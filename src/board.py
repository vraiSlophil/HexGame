from src.boxes import Box


# Rouge : bas en haut, couleur : -1   /   Bleu : gauche à droite, couleur : 1
# Cette classe a été développée par tout le monde mais en majorité Nathan O et Martin
class Board:
    def __init__(self, size=4):
        # dictionnaire qui contient les coordonnées x et y en tuple en clé et une instance de box en valeur
        self.__board = {(x, y): Box(x, y, size, self) for y in range(size + 1) for x in range(size + 1)}
        # n taille du plateau
        self.__size = size
        self.__finished = False

        self.__left = [(0, y) for y in range(size + 1)]
        self.__right = [(size, y) for y in range(size + 1)]
        self.__up = [(x, 0) for x in range(size + 1)]
        self.__down = [(x, size) for x in range(size + 1)]

    def is_finished(self):
        return self.__finished

    def set_finished(self, value: bool):
        self.__finished = value

    def is_full(self):
        for box_instance in self.__board.values():
            if box_instance.get_color() == 0:
                return False


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

    def update(self):
        if self.win_team(1):
            print("Le joueur bleu a gagné")
            self.set_finished(True)
        elif self.win_team(-1):
            print("Le joueur rouge a gagné")
            self.set_finished(True)
        else:
            self.set_finished(False) if self.is_finished() or self.is_full() else None
            print("Le jeu n'est pas fini")

            
    # La première version de cette fonction était faite par Martin mais ne fonctionnait pas alors Nathan O l'a refaite entièrement
    def win_team(self, color):
        checked_boxes = set()  # Ici on utilise un set pour éviter de vérifier plusieurs fois la même case car la
        # spécificité du set est de ne pas contenir de doublons
        for coordinates, box_instance in self.__board.items():
            if box_instance.get_color() == color:
                if coordinates not in checked_boxes:
                    return self.__recu(coordinates, color, checked_boxes)
        return False
    # Celle ci aussi
    def __recu(self, coordinates, color, checked_boxes):
        checked_boxes.add(coordinates)
        print(color)
        print(str(checked_boxes))
        if color == -1 and coordinates in (self.__up + self.__down) and any((x, y) in self.__up for x, y in checked_boxes) and any((x, y) in self.__down for x, y in checked_boxes):
            return True
        if color == 1 and coordinates in (self.__left + self.__right) and any((x, y) in self.__left for x, y in checked_boxes) and any((x, y) in self.__right for x, y in checked_boxes):
            return True
        for neighbour in self.__board[coordinates].get_neighbours_same_color():
            if neighbour.get_coords() not in checked_boxes:
                return self.__recu(neighbour.get_coords(), color, checked_boxes)
        return False
