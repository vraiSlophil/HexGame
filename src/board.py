from src.boxes import Box


# Rouge : bas en haut, couleur : -1   /   Bleu : gauche à droite, couleur : 1
class Board:
    def __init__(self, size=4):
        # dictionnaire qui contient les coordonnées x et y en tuple en clé et une instance de box en valeur
        self.__board = {(x, y): Box(x, y, size, self) for y in range(size + 1) for x in range(size + 1)}
        # n taille du plateau
        self.__size = size

    def get_board(self):
        return self.__board

    def get_tour(self):
        temp = 0
        for box_instance in self.__board.values():
            temp += box_instance.get_color()
        if temp == 0:
            return 1
        return -1

    def get_size(self):
        return self.__size

    def win_team(self, color):
        checked_boxes = set()
        for coordinates, box_instance in self.__board.items():
            if box_instance.get_color() == color:
                if coordinates not in checked_boxes:
                    if self.__dfs(coordinates, color, checked_boxes):
                        return True
        return False

    def __dfs(self, coordinates, color, checked_boxes):
        checked_boxes.add(coordinates)
        if (color == 1 and coordinates[0] == self.__size) or (color == -1 and coordinates[1] == self.__size):
            return True
        for neighbour in self.__board[coordinates].get_neighbours_same_color():
            if neighbour.get_coords() not in checked_boxes:
                if self.__dfs(neighbour.get_coords(), color, checked_boxes):
                    return True
        return False
