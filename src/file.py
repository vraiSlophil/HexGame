class File:
    def __init__(self):
        self.__data = []
        self.__tete = 0

    def enfiler(self, e):
        self.__data.append(e)

    def defiler(self):  # lance IndexError si la File est vide
        if self.est_vide():
            raise (IndexError("file vide"))
        if self.__tete > len(self):
            self.__data = self.__data[self.__tete:]
            self.__tete = 0
        # Maintenant, on ne procède au décalage qu'une fois de temps en temps
        self.__tete += 1
        return self.__data[self.__tete - 1]

    def est_vide(self):
        return len(self) == 0

    def __len__(self):
        return len(self.__data) - self.__tete
