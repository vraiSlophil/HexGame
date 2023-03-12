# classe pour représenter un plateau de jeu de hex, de 5x5 cases
from clazz import boxes


# Rouge : bas en haut, couleur : -1 / Bleu : gauche à droite, couleur : 1
class Board:
    def __init__(self, size=3):
        # dictionnaire qui contient les coordonnées x et y en tuple en clé et une instance de box en valeur
        self.__board = {(x, y): boxes.Box(x, y, size, self) for y in range(size + 1) for x in range(size + 1)}
        # n taille du plateau
        self.__size = size

    def __hash__(self):
        return hash((frozenset(self.__board.items()), self.__size))

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.__board == other.__board and self.__size == other.__size

    def get_board(self):
        return self.__board

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

    def win_team(self,
                 nb_color=0):  # renvoie True si la couleur passée en argument gagne et False sinon. renvoie False si la couleur est 0
        if nb_color == 0:
            return False

        mem_boxes = []
        # On parcours d'abord le plateau pour mémoriser les coordonnées des boxes se situant sur une extrémité du plateau
        for coords, b in self.__board.items():  # b est une boxe
            if b.get_color() == nb_color:
                if nb_color == -1 and b.get_y() == 0:  # pour mémoriser les coordonnées des boxes rouges se trouvant en bas du plateau
                    mem_boxes.append(b.get_coords())
                if nb_color == 1 and b.get_x() == 0:  # pour mémoriser les coordonnées des boxes bleues se trouvant à gauche du plateau
                    mem_boxes.append(b.get_coords())

        # On regarde les voisins de chaque boxe dont les coordonnées se trouvent dans mem_boxes et rajoute les coordonnées de ces voisins dans mem_boxes
        nb_new_elements = len(mem_boxes) - 1
        for i in range(nb_new_elements):
            for coords_neighbours in self.__board[mem_boxes[i]].get_neighbours_same_color():
                if nb_color == -1 and coords_neighbours[1] == self.__size:
                    return True
                if nb_color == 1 and coords_neighbours[0] == self.__size:
                    return True
                if coords_neighbours not in mem_boxes:
                    mem_boxes.append(coords_neighbours)
                    nb_new_elements += 1
        return False

    def play(self, coordinates, color):
        if self.__board[coordinates] != 0 or self.__board[coordinates] == color:
            return False
        self.__board[coordinates].set_color(color)
        return True
