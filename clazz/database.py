import mariadb

import main


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

    def board_to_string(self):
        L = ""
        for box_instance in main.board.values():
            if len(L) != self.__size ** self.__size:
                L.append(str(box_instance.get_color()) + ",")
            else:
                L.append(str(box_instance.get_color()))
        return L
        # exemple de return : "0,0,0,0,0,0,1,0,0,0,0,-1,0,0,0,0"

    def string_to_board(self, L):
        if self.board_to_string() == L:
            return main.board
        lst = [int(x) for x in L.split(',')]
        index = 0
        for box_instance in main.board.values():
            if box_instance.get_color() != lst[index]:
                box_instance.set_color(lst[index])
            index += 1
        return main.board


