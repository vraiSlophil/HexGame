import pygame
from sprites.sprite_library import hexa1, hexa_1, hexa0

pygame.init()


# classe écran
class Screen:
    def __init__(self, width, height, list_boxes, img_hex):
        self.__width = width  # largeur de l'écran
        self.__height = height  # hauteur de l'écran
        self.list_boxes = list_boxes  # la liste des instances boxes
        self.__screen = pygame.display.set_mode((self.__width, self.__height))  # création de l'affichage
        pygame.display.set_caption("Hex")  # juste un titre pour la fenêtre
        self.box_sprite_group = pygame.sprite.Group()  # on fait des groupes de sprites pour les update
        self.elements_group = pygame.sprite.Group()    # plus facilement
        self.img_hex = img_hex  # une image d'hexagone vide
        self.imgsize = 64  # taille de l'image en pixels

        self.grid = GridRect(100, 100)  # des valeurs bateau
        self.elements_group.add(self.grid)  # ajoute l'élément grid dans le groupe des éléments de l'écran
        # apparemment, self.grid n'est pas valide pour un groupe
        for i in self.list_boxes:  # on relie chaque instance box avec une instance de sprite
            sprite_box = BoxSprite(i, self.img_hex, self.imgsize)
            self.box_sprite_group.add(sprite_box)

    def get_screen(self):
        return self.__screen

    def update(self):
        self.__screen.fill((0, 0, 0))  # on remplit l'écran de noir pour effacer l'image précédente
        # mettre à jour tous les éléments
        self.box_sprite_group.update()
        self.elements_group.update()
        self.elements_group.draw(self.__screen)  # on imprime les sprites sur la surface
        self.box_sprite_group.draw(self.__screen)


class GridRect(pygame.sprite.Sprite):  # ca sera l'espace contenant la grille de jeu
    def __init__(self, width, length):
        super().__init__(self)
        self.image = pygame.Rect(0, 0, width, length)  # temporaire



class BoxSprite(pygame.sprite.Sprite):  # l'instance graphique d'une case
    def __init__(self, box, img, imgsize):
        pygame.sprite.Sprite.__init__(self)
        self.image = img  # on charge l'image de base
        self.image = pygame.transform.scale(self.image, (imgsize, imgsize))  # on ajuste l'image a la bonne taille
        self.rect = self.image.get_rect()  # on récupère les dimensions de l'image pour en faire celles du sprite
        self.box = box  # on garde en mémoire l'instance non graphique de la case
        self.rect.x = -1*self.box.get_x()*imgsize  # imgsize : dimensions de l'image dans le rendu
        self.rect.Y = self.box.get_y()*imgsize  # Il faudra changer après pour avoir une grille en losange

    def update(self):
        color = self.box.get_color()  # on change la case de couleur en fonction de la valeur de son instance
        if color == 1:                # non-graphique
            self.image = hexa1
        elif color == 0:
            self.image = hexa0
        else:
            self.image = hexa_1


def text_image(text, police, colorRGB): # Pourquoi cette fonction ? ->
    image = police.render(text, 1, colorRGB)  # crée une image contenant du texte avec une certaine couleur
    return image
