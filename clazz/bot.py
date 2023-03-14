from clazz import file


# Le bot est de couleur rouge
class Bot:
    def __init__(self, board_instance):
        self.__color = -1  # rouge
        # self.__n = 4
        self.__tour = False  # True si c'est au tour du bot, False sinon
        self.__board_instance = board_instance

        self.__file = file.File()

        self.__mem_hex_IA = dict()
        self.__win_mem_hex_IA = []
        self.__win_moves_IA = dict()

        self.__mem_hex_player = dict()

        # self.__sides = (False, False) #Cotés objectifs atteints ou non, (Bas, Haut)
        # self.__start_box_coordinates = []
        # self.__end_box_coordinates = []
        # self.__player_sides = (False, False) #Cotés objectifs atteints ou non, (Gauche, Droite)
        # self.__left_box_coordinates_player = []
        # self.__right_box_coordinates_player = []

    def place_box(self):
        if self.__tour:
            pass

    def replace_blue_box(self):
        if self.__tour:
            pass

    # def best_move(self):
    # board = self.__board_instance.get_board()
    # if board in mem_hex:
    #        return mem_hex[board]
    # if board.win_team()[0] == True:
    #    mem_hex[board] = board.win_team()[1]

    def resoud_hex(self):
        mem_hex = self.__mem_hex_IA   #qui est un dictionnaire
        board = self.__database_instance.board_to_string(self.__board_instance.get_board().copy())
        #board est une liste de 16 éléments de type [1,1,-1,0,0,...,1]
        board_size = self.__board_instance.get_size()
        if board in mem_hex:
            return mem_hex[board]
        # on teste si la partie est finie
        if self.__board_instance.win_team(-1):
            mem_hex[board] = -1
            return -1
        elif self.__board_instance.win_team(1):
            mem_hex[board] = 1
            return 1
        # on cherche à qui est le tour
        nb_blue, nb_red = 0, 0
        for coordinates, box_instance in board.items():
            if box_instance.get_color() == 1:
                nb_blue += 1
            elif box_instance.get_color() == -1:
                nb_red += 1

        tour = nb_red == nb_blue  # indique si c'est au tour de l'IA ou du joueur
        joueur = 1 if tour else -1  # joueur dont c'est le tour
        # on fait la liste des coups possibles, c'est à dire les nouveaux plateaux obtenables
        L = []
        for i in range(board_size ** board_size):
            if board[i] == 0:
                # construire un plateau avec un nouveau pion dans cette case
                nouveau = board[0:i] + (joueur,) + board[i + 1:]
                # le mettre dans L
                L.append(nouveau)
        # on cherche l'eval max si c'est au tour de croix, et l'eval min si c'est au tour de rond
        evaluation = -joueur
        plateau_gagnant = [L[0]]
        for p in L:
            e = self.resoud_hex(p)
            if tour and e > evaluation:
                evaluation = e
                if len(p) <= plateau_gagnant[-1]:
                    plateau_gagnant.append(p)
            elif (not tour) and e < evaluation:
                evaluation = e
                if len(p) <= plateau_gagnant[-1]:
                    plateau_gagnant.append(p)
        mem_hex[board] = evaluation
        return (evaluation,plateau_gagnant)



    # def path_finding(self):
    #     board = self.__board_instance.get_board()
    #
    #     for coordinates, box_instance in board.items():
    #         if box_instance.get_y() == 0 and box_instance.get_color() == self.__color:
    #             self.__start_box_coordinates.append(coordinates)
    #             self.__sides = (True, self.__sides[1])
    #
    #         if box_instance.get_y() == self.__board_instance.get_size() and box_instance.get_color() == self.__color:
    #             self.__end_box_coordinates.append(coordinates)
    #             self.__sides = (self.__sides[1], True)
    #
    #     if self.__sides[0] and self.__sides[1]:
    #         pass
    #
    #     for coordinates, box_instance in board.items():

    # index = 0
    # def best_neighbour(self, coordinates_tuple, box_instance):
    #     L = []
    #     box = box_instance
    #     if len(box_instance.get_free_neighbours()) == 0:
    #         return L
    #     for i in box.get_box_access:
    #         L.append()
    #
    # def path_finding(self, x=0, y=0, box_instance=None):
    #     board = self.__board_instance.get_board()
    #     board_size = self.__board_instance.get_size()
    #     for coords in board.keys(): #coords est un tuple de coordonées : (x, y)
    #         #(k, l) sont les coords des cases voisines libres dont on a pas déjà déterminé les voisins libres
    #         self.__mem_hex_IA[coords] = [(k, l) for (k, l) in board[coords].get_free_neigbours() + board[coords].get_neigbours_same_color(-1) if (k, l) not in self.__mem_hex_IA.keys()]
    #     for coordinates, box_instance in board.items():
    #         if box_instance.get_color() == self.__color*(-1):
    #             self.__mem_hex_player[coordinates] = [(k, l) for (k, l) in board[coordinates].get_free_neigbours() + board[coordinates].get_neigbours_same_color(0) if (k, l) not in self.__mem_hex_player.keys()]
    #     best_moves_AI = []
    #     best_moves_player = []
    #     inter = [(board_size, 0)]
    #     fin = False
    #     while not fin:
    #         for k,v in self.__mem_hex_IA.items(): # k est un tuple de coordonnées (x, y) et v est une liste de tuples de coordonnées des voisins de la clé (x, y)
    #             if k in self.__mem_hex_IA[inter[-1]:
    #             inter.append(k)
    #             #
    #             #
    #             #
    #             #
    #             # for k, v in self.__mem_hex_player.items():  # k est un tuple de coordonnées (x, y) et v est une liste de tuples de coordonnées de coups possibles (x, y)
    #             #     if len(v) != 0:
    #             #         if k[1] < 2:
    #             #             best_moves_AI.append()
    #
    #
    # def path_finding_player(self):
    #     board = self.__board_instance.get_board()
    #
    #     for coordinates, box_instance in board.items():
    #         if box_instance.get_x() == 0 and box_instance.get_color() == self.__color*(-1):
    #             self.__start_box_coordinates.append(coordinates)
    #             self.__sides = (True, self.__sides[1])
    #         if box_instance.get_x() == self.__board_instance.get_size() and box_instance.get_color() == self.__color*(-1):
    #             self.__end_box_coordinates.append(coordinates)
    #             self.__sides = (self.__sides[1], True)
