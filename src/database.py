import mariadb

from src.bot import Bot


class Database:
    def __init__(self):
        self.__connect = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            # port=3307,
            port=3306,
            database="HexGame"
        )

    # def create_box(self, x, y, box_access, color):
    #     self.get_connect().cursor().execute("INSTERT INTO HexGame(x,y,box_access,color) VALUES (?,?,?,?);", (x, y, box_access, color))

    def get_connect(self):
        return self.__connect

    # exemple de return : "0,0,0,0,0,0,1,0,0,0,0,-1,0,0,0,0,"
    def board_to_string(self, board_instance):
        S = ""  # S est un string
        for box_instance in board_instance.get_board().values():
            S += (str(box_instance.get_color()) + ",")
        return S

    # return une nouvelle instance de board
    def string_to_board(self, board_instance, L):
        if self.board_to_string(board_instance) == L:
            return board_instance
        lst = [int(x) for x in L.split(',')]
        index = 0
        for box_instance in board_instance.get_board().values():
            if box_instance.get_color() != lst[index]:
                box_instance.set_color(lst[index])
            index += 1
        return board_instance

    def board_to_int(self, board_dict):
        board_int = []
        for box_instance in board_dict.values():
            board_int.append(box_instance.get_color())
        return board_int

    def int_to_string(self, board_compact_list):
        string = ""
        for box_color in board_compact_list:
            string += box_color + ","
        return string

    def string_to_int(self, board_compact_string):
        board_int = []
        for box_instance in board_compact_string.split(','):
            board_int.append(int(box_instance))
        return board_int

    def insert_board(self, board):
        self.__connect().cursor().execute("INSERT INTO board(board_state, evaluation, player, diff) VALUES (?,?,?);",
                                          (self.board_to_string(board), Bot.resoud_hex(board)), board.get_tour())

    def select_next_boards_to_IA(self, board):  # renvoie les plateaux avancés d'un coup qui vont gagner sous la forme de liste de liste en int
        plateaux = list(self.__connect().cursor().execute(
            "SELECT board_state FROM board WHERE evaluation = 1 AND player = -1 AND ? = board_state;",
            (self.int_to_string(Bot.get_L()))))
        plateaux_board = []
        for p in plateaux:
            plateaux_board.append(self.string_to_board(p))
        return plateaux_board
