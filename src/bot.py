import random


# Cette classe a été majoritairement faite par Martin et Nathan L
class Bot:
    def __init__(self, board_instance):
        self.color = -1  # rouge
        self.board = board_instance

    def play(self):
        # Si on arrive ici, cela signifie que le plateau n'a pas été trouvé dans la base de données ou qu'il n'y a
        # pas de meilleur coup connu. On utilise alors un algorithme pour déterminer le meilleur coup possible
        best_x, best_y = self.get_best_move()
        self.board.get_board()[best_x, best_y].play()

    # Ici c'est sensé être la fonction dans laquelle l'IA choisit le meilleur coup mais ça a été trop dur
    def get_best_move(self):
        board_size = self.board.get_size()
        x, y = (random.randint(0, board_size), random.randint(0, board_size))
        while self.board.get_board()[(x, y)].get_color() != 0:
            x, y = (random.randint(0, board_size), random.randint(0, board_size))
        return x, y

    # def minimax(board, depth, maximizingPlayer):
    #     if depth == 0 or game_over(board):
    #         return evaluate(board)
    #
    #     if maximizingPlayer:
    #         maxEval = float('-inf')
    #         for move in get_all_possible_moves(board):
    #             eval = minimax(make_move(board, move), depth - 1, False)
    #             maxEval = max(maxEval, eval)
    #         return maxEval
    #     else:
    #         minEval = float('inf')
    #         for move in get_all_possible_moves(board):
    #             eval = minimax(make_move(board, move), depth - 1, True)
    #             minEval = min(minEval, eval)
    #         return minEval