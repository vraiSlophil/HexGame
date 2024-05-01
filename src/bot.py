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

        if self.board.get_tour() == self.color and not self.board.is_finished():
            self.board.update()

    def get_best_move(self):
        board_size = self.board.get_size()
        center = (board_size // 2, board_size // 2)

        # Si le plateau est vide, prendre la case du milieu
        if all(self.board.get_board()[(x, y)].get_color() == 0 for x in range(board_size) for y in range(board_size)):
            return center

        # Si la case du centre est prise, choisir une case proche du centre
        if self.board.get_board()[center].get_color() != 0:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                x, y = center[0] + dx, center[1] + dy
                if 0 <= x < board_size and 0 <= y < board_size and self.board.get_board()[(x, y)].get_color() == 0:
                    return x, y

        # # Calculer le chemin le plus court pour le bot en passant par le point central
        # shortest_path_bot = self.board.shortest_path((0, 0), center, self.color)
        #
        # # Calculer les chemins les plus probables pour le joueur
        # shortest_path_player = self.board.shortest_path((0, 0), center, -self.color)
        #
        # # Calculer un indice de risque basé sur les chemins calculés précédemment
        # risk_index = len(shortest_path_player) / len(shortest_path_bot)
        #
        # # Si l'indice de risque est élevé, jouer un coup qui bloque le joueur
        # if risk_index > 1:
        #     for move in shortest_path_player:
        #         if self.board.get_board()[move].get_color() == 0:
        #             return move
        #
        # # Sinon, jouer un coup qui avance le bot vers la victoire
        # for move in shortest_path_bot:
        #     if self.board.get_board()[move].get_color() == 0:
        #         return move
        #
        # # Si aucun coup n'est disponible, choisir un coup aléatoire
        # x, y = (random.randint(0, board_size), random.randint(0, board_size))
        # while self.board.get_board()[(x, y)].get_color() != 0:
        #     x, y = (random.randint(0, board_size), random.randint(0, board_size))
        # return x, y