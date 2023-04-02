class ColorError(Exception):
    pass

# Ce fichier a été majoritairement fait par Martin et Nathan L

class Box:
    def __init__(self, x, y, size, board_instance):
        self.__x = x
        self.__y = y
        self.__coords = (x, y)
        self.__board_instance = board_instance
        self.__box_access = [(x + 1, y), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x, y - 1), (x + 1, y - 1)]
        self.__color = 0  # 0 quand il n'y a aucune couleur, 1 pour bleu, -1 pour rouge

        valid_coords = []
        for coordinates in self.__box_access:
            if (0 <= coordinates[0] <= size) and (0 <= coordinates[1] <= size):
                valid_coords.append(coordinates)
        self.__box_access = valid_coords

        #cette fonction a été faite pour le debuguage afin que la console ne nous affiche plus les adresses mémoires mais les infos des box
    def __str__(self):
        return "[Coordonnées : " + str(self.__coords) + " | Couleur : " + str(self.__color) + " | Accès : " + str(self.__box_access) + "]"

    def get_box_access(self):
        return self.__box_access

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_coords(self):
        return self.__coords

    def get_color(self):
        return self.__color

    def get_neighbours_same_color(self):  # Renvoie les coordonnées des voisins ayant la même couleur. S'il n'a pas de voisin de même couleur, renvoie une liste vide
        neighbours_same_color = []
        for available_boxes in self.__box_access:
            for coordinates, box_instance in self.__board_instance.get_board().items():
                if coordinates == available_boxes:
                    if self.__board_instance.get_board()[coordinates].get_color() == self.get_color():
                        neighbours_same_color.append(box_instance)
        return neighbours_same_color

    def get_free_neighbours(self):  # renvoie les coordonnées des cases vides voisines
        neighbours = []
        for available_boxes in self.__box_access:
            for coordinates, box_instance in self.__board_instance.get_board().items():
                if coordinates == available_boxes:
                    if self.__board_instance.get_board()[coordinates].get_color() == 0:
                        neighbours.append(box_instance.get_coords())
        return neighbours

    def set_color(self, number_color):
        assert number_color in [-1, 0, 1], ColorError("Ce numéro de couleur n'existe pas")
        self.__color = number_color

    def play(self):
        if self.get_color() != 0:
            return
        self.set_color(self.__board_instance.get_tour())
