# classe pour représenter un plateau de jeu de hex, de 5x5 cases
from src import boxes
from src.file import File


# Rouge : bas en haut, couleur : -1   /   Bleu : gauche à droite, couleur : 1
class Board:
    def __init__(self, size=4):
        # dictionnaire qui contient les coordonnées x et y en tuple en clé et une instance de box en valeur
        self.__board = {(x, y): boxes.Box(x, y, size, self) for y in range(size + 1) for x in range(size + 1)}
        # n taille du plateau
        self.__size = size
        self.__win_mem_hex = []  # liste pour stocker les coordonnées des voisins de même couleur
        self.__file = File()

    def __hash__(self):
        return hash((frozenset(self.__board.items()), self.__size))

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.__board == other.__board and self.__size == other.__size

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

    def get_tour(self):
        nb_blue, nb_red = 0, 0
        for coordinates, box_instance in self.__board.items():
            if box_instance.get_color() == 1:
                nb_blue += 1
            elif box_instance.get_color() == -1:
                nb_red += 1
        tour = nb_red == nb_blue  # indique si c'est au tour de l'IA ou du joueur
        return 1 if tour else -1  # joueur dont c'est le tour

    def win_team(self, color=0):
        if color == 0:
            return False
        available_path = self.__file  # inter est une file de tuples de coordonnées
        for box_instance in self.get_board().values():
            if color == -1:
                if box_instance.get_color() == -1 and box_instance.get_y() == 0:  # si la couleur de la case est rouge
                    self.__win_mem_hex.append(box_instance)
            else:
                if box_instance.get_color() == 1 and box_instance.get_x() == 0:  # si la couleur de la case est bleue
                    self.__win_mem_hex.append(box_instance)
        print("available_path : [" + ", ".join(str(i) for i in available_path.get_data()) + "]")
        print("win_mem_hex : [" + ", ".join(str(e) for e in self.__win_mem_hex) + "]")
        for box_instance in self.__win_mem_hex:
            available_path.enfiler(box_instance)
            while not available_path.est_vide():
                case = available_path.defiler()  # case est une box
                for box_instance_neighbour in case.get_neighbours_same_color():
                    if box_instance_neighbour not in self.__win_mem_hex:
                        available_path.enfiler(box_instance_neighbour)
                        self.__win_mem_hex.append(box_instance_neighbour)
                if color == -1 and case.get_y() == self.get_size() - 1:
                    return True
                if color == 1 and case.get_x == self.get_size() - 1:
                    return True
        print("available_path : [" + ", ".join(str(i) for i in available_path.get_data()) + "]")
        print("win_mem_hex : [" + ", ".join(str(e) for e in self.__win_mem_hex) + "]")
        return False