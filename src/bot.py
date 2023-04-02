import random


class Bot:
    def __init__(self, board_instance, database_instance):
        self.color = -1  # rouge
        self.board = board_instance
        self.database = database_instance

    def play(self):
        best_x, best_y = self.database.get_best_move(self.board)
        if best_x is not None and best_y is not None:
            a = self.board.get_board()[best_x, best_y].play()
            print(a)
            return

        # Si on arrive ici, cela signifie que le plateau n'a pas été trouvé dans la base de données ou qu'il n'y a pas de meilleur coup connu.
        # On utilise alors un algorithme pour déterminer le meilleur coup possible
        best_x, best_y = self.get_best_move()
        self.board.get_board()[best_x, best_y].play()
        self.database.add_board_state(self.board, best_x, best_y)

    def get_best_move(self):
        board_size = self.board.get_size()
        x, y = (random.randint(0, board_size), random.randint(0, board_size))
        while self.board.get_board()[(x, y)].get_color() == 0:
            x, y = (random.randint(0, board_size), random.randint(0, board_size))
        return x, y
