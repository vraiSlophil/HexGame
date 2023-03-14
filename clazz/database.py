import mariadb

class Database:
    def __init__(self):
        self.__connect = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3307,
            database="HexGame"
        )

    # def create_box(self, x, y, box_access, color):
    #     self.get_connect().cursor().execute("INSTERT INTO HexGame(x,y,box_access,color) VALUES (?,?,?,?);", (x, y, box_access, color))

    def get_connect(self):
        return self.__connect

    # exemple de return : "0,0,0,0,0,0,1,0,0,0,0,-1,0,0,0,0"
    def board_to_string(self, board_instance):
        L = ""
        for box_instance in board_instance.get_board().values():
            if len(L) != board_instance.get_size() ** board_instance.get_size():
                L.append(str(box_instance.get_color()) + ",")
            else:
                L.append(str(box_instance.get_color()))

        return L

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


