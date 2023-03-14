class Box:
    def __init__(self, x, y, size, board_instance):
        self.__x = x
        self.__y = y
        self.__coords = (x, y)
        self.__board_instance = board_instance
        self.__box_access = [(x + 1, y), (x - 1, y), (x - 1, y - 1), (x, y + 1), (x, y - 1), (x + 1, y + 1)]
        self.__color = 0  # 0 quand il n'y a aucune couleur, 1 pour bleu, -1 pour rouge

        if self.__x - 1 < 0:
            self.__box_access.remove((self.__x - 1, self.__y))
            self.__box_access.remove((self.__x - 1, self.__y - 1))
        if self.__y - 1 < 0:
            self.__box_access.remove((self.__x, self.__y - 1))
        if self.__x + 1 > size:
            self.__box_access.remove((self.__x + 1, self.__y))
            self.__box_access.remove((self.__x + 1, self.__y + 1))
        if self.__y + 1 > size:
            self.__box_access.remove((self.__x, self.__y + 1))

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

    def get_neighbours_same_color(self):  # renvoie les coordonnées des voisins ayant la même couleur. S'il n'a pas de voisin de même couleur, renvoie une liste vide
        r = []
        for i in self.__box_access:
            for k, v in self.__board_instance.get_board().items():
                if k == i:
                    if self.__board_instance.get_board()[k].get_color() == self.get_color():
                        r.append(i)
        return r


    def get_free_neighbours(self):  # renvoie les coordonnées des cases vides voisines
        r = []
        for i in self.__box_access:
            for k, v in self.__board_instance.get_board().items():
                if k == i:
                    if self.__board_instance.get_board()[k].get_color() == 0:
                        r.append(i)
        return r


    def set_color(self, number_color):
        assert number_color in [-1, 0, 1], "Ce numéro de couleur n'existe pas"
        self.__color = number_color

    def __hash__(self):
        return hash((self.__x, self.__y, self.__coords, self.__board_instance, self.__color, frozenset(self.__box_access)))

    def __eq__(self, other):  # other est un objet que l'on compare à l'instance de Box
        if not isinstance(other, Box):
            return False
        return self.__x == other.get_x() and self.__y == other.get_y() and self.__coords == other.get_coords() and self.__board_instance == other.__board_instance and self.__color == other.get_color() and frozenset(self.__box_access) == frozenset(other.get_box_access())
