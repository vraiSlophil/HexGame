import mariadb


class Database:
    def __init__(self):
        self.connect = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3307,
            database="HexGame"
        )

    def __del__(self):
        self.connect.close()

    def get_board_state(self, board_instance):
        cursor = self.connect.cursor()
        cursor.execute("SELECT board_state FROM board WHERE board_state=?", (self.board_to_string(board_instance),))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
        # return cursor.fetchall()

    def add_board_state(self, board_instance, best_x, best_y):
        cursor = self.connect.cursor()
        cursor.execute("INSERT INTO board (board_state, best_x, best_y) VALUES (?, ?, ?)",
                       (self.board_to_string(board_instance), best_x, best_y))
        self.connect.commit()

    def get_best_move(self, board_instance):
        cursor = self.connect.cursor()
        cursor.execute("SELECT best_x, best_y FROM board WHERE board_state=?", (self.board_to_string(board_instance),))
        result = cursor.fetchone()
        if result:
            return result[0], result[1]
        else:
            return None, None

    def board_to_string(self, board_instance):
        S = ""  # S est un string
        for box_instance in board_instance.get_board().values():
            S += (str(box_instance.get_color()) + ",")
        return S
