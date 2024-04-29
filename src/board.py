from queue import PriorityQueue
from src.boxes import Box


# Rouge : bas en haut, couleur : -1   /   Bleu : gauche à droite, couleur : 1
class Board:
    def __init__(self, size=4):
        # dictionnaire qui contient les coordonnées x et y en tuple en clé et une instance de box en valeur
        self.__board = {(x, y): Box(x, y, size, self) for y in range(size + 1) for x in range(size + 1)}
        # n taille du plateau
        self.__size = size
        self.__finished = False

        self.__left = [(0, y) for y in range(size + 1)]
        self.__right = [(size, y) for y in range(size + 1)]
        self.__up = [(x, 0) for x in range(size + 1)]
        self.__down = [(x, size) for x in range(size + 1)]

    def is_finished(self):
        return self.__finished

    def set_finished(self, value: bool):
        self.__finished = value

    def is_full(self):
        for box_instance in self.__board.values():
            if box_instance.get_color() == 0:
                return False
        return True

    def get_board(self):
        return self.__board

    def get_tour(self):
        temp = 0
        for box_instance in self.__board.values():
            temp += box_instance.get_color()
        if temp == 0:
            return 1
        return -1

    def get_size(self):
        return self.__size

    def update(self):
        if self.win_team(1):
            self.set_finished(True)
            print("Team 1 has won!")
        elif self.win_team(-1):
            self.set_finished(True)
            print("Team -1 has won!")
        else:
            self.set_finished(False) if self.is_finished() or self.is_full() else None

    def shortest_path(self, start, end, color):
        print(f"Calculating shortest path from {start} to {end} for color {color}")
        # Initialisation de la file de priorité et du dictionnaire des distances
        priority_queue = PriorityQueue()
        distances = {node: float('infinity') for node in self.__board.keys()}
        distances[start] = 0

        # Ajout du nœud de départ à la file de priorité
        priority_queue.put((0, start))

        while not priority_queue.empty():
            # Récupération du nœud avec la plus petite distance
            current_distance, current_node = priority_queue.get()

            # Si le nœud actuel est le nœud de fin, nous avons trouvé le chemin le plus court
            if current_node == end:
                return distances[end]

            # Sinon, nous mettons à jour les distances de tous les voisins du nœud actuel
            for neighbour in self.__board[current_node].get_neighbours_same_color():
                if neighbour.get_color() == color:
                    new_distance = distances[current_node] + 1
                    if new_distance < distances[neighbour.get_coords()]:
                        distances[neighbour.get_coords()] = new_distance
                        priority_queue.put((new_distance, neighbour.get_coords()))

        # Si aucun chemin n'a été trouvé, nous retournons l'infini
        return float('infinity')

    def win_team(self, color):
        print(f"Checking if team {color} has won")
        # Vérification si l'équipe a des cases sur les deux côtés du plateau
        if color == 1:
            if not any(self.__board[coordinates].get_color() == color for coordinates in self.__left) or \
                    not any(self.__board[coordinates].get_color() == color for coordinates in self.__right):
                return False
        elif color == -1:
            if not any(self.__board[coordinates].get_color() == color for coordinates in self.__up) or \
                    not any(self.__board[coordinates].get_color() == color for coordinates in self.__down):
                return False

        # Recherche du chemin le plus court entre une case sur un côté et une case sur l'autre côté
        if color == 1:
            shortest = min(self.shortest_path(start, end, color)
                           for start in self.__left
                           for end in self.__right
                           if self.__board[start].get_color() == color and self.__board[end].get_color() == color)
        elif color == -1:
            shortest = min(self.shortest_path(start, end, color)
                           for start in self.__up
                           for end in self.__down
                           if self.__board[start].get_color() == color and self.__board[end].get_color() == color)

        # Vérification si le chemin le plus court a une longueur suffisante
        return shortest <= self.__size + 1