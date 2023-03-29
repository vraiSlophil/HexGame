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
        pygame.display.set_caption("Hex game")  # juste un titre pour la fenêtre
        self.__box_sprite_group = pygame.sprite.Group()  # on fait des groupes de sprites pour les update
        self.__elements_group = pygame.sprite.Group()  # plus facilement
        self.__img_hex = img_hex  # une image d'hexagone vide
        self.__imgsize = 64  # taille de l'image en pixels

        for box_instance in self.list_boxes.values():  # on relie chaque instance box avec une instance de sprite
            sprite_box = BoxSprite(box_instance, self.__img_hex, self.__imgsize)
            self.__box_sprite_group.add(sprite_box)

        #
        # self.button1 = Button((200, 100), (64, 64), "test", "")  # un bouton de test
        # self.__elements_group.add(self.button1)
        #
        # self.button2 = Button((200, 300), (64, 64), "test", "")  # un bouton de test
        # self.__elements_group.add(self.button2)

    def get_screen(self):
        return self.__screen

    def get_box_sprite_group(self):
        return self.__box_sprite_group

    def get_elements_group(self):
        return self.__elements_group

    def update(self):
        self.__screen.fill((255, 255, 255))  # on remplit l'écran d'une couleur pour effacer l'image précédente
        # mettre à jour tous les éléments
        self.__box_sprite_group.update()
        self.__elements_group.update()
        # on imprime les sprites sur l'écran
        self.__box_sprite_group.draw(self.__screen)
        self.__elements_group.draw(self.__screen)


class BoxSprite(pygame.sprite.Sprite):  # l'instance graphique d'une case
    def __init__(self, box_instance, img, imgsize):
        pygame.sprite.Sprite.__init__(self)
        self.image = img  # il faudra mettre 'img = pygame.image.load("imagedelhexagone")' pour éviter d'aller chercher
        # dans la memoire trop souvent
        self.image = pygame.transform.scale(self.image, (imgsize, imgsize))  # on ajuste l'image a la bonne taille
        self.rect = self.image.get_rect()  # on récupère les dimensions de l'image pour en faire celles du sprite
        self.box_instance = box_instance
        x = box_instance.get_x()
        y = box_instance.get_y()
        self.rect.x = (x * imgsize) + (32 * y)  # imgsize : dimensions de l'image dans le rendu
        self.rect.y = (y * imgsize)
        self.img_size = imgsize

    def play(self, board_instance):
        if self.box_instance.get_color() == 0: # on vérifie que la case n'a pas déjà une couleur
            self.box_instance.set_color(board_instance.get_tour()) # on change la case de couleur en fonction de la valeur de son instance

    def update(self):
        color = self.box_instance.get_color()  # on change la case de couleur en fonction de la valeur de son instance
        if color == 1:  # non-graphique
            self.image = hexa1
            self.image = pygame.transform.scale(self.image, (self.img_size, self.img_size))
        elif color == 0:
            self.image = hexa0
            self.image = pygame.transform.scale(self.image, (self.img_size, self.img_size))
        else:
            self.image = hexa_1
            self.image = pygame.transform.scale(self.image, (self.img_size, self.img_size))


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, category, text_to_display):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.size = size
        self.category = category  # pour déterminer l'action à faire
        self.image = hexa0  # pour charger l'image du cadre, à changer après
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.police = pygame.font.SysFont("arial", 15)  # on charge la police d'écriture, on pourra changer
        self.text = text_image(text_to_display, self.police, (0, 0, 0))  # on charge le texte
        self.image.blit(self.text, (self.rect.width / 2 - self.text.get_width() / 2,  # on colle le texte sur le
                                    self.rect.height / 2 - self.text.get_height() / 2))  # milieu du bouton

    def update(self):
        pass

def text_image(text, police, colorRGB):  # attention, il faudrait coller ça sur la surface d'un SPRITE
    text = police.render(text, True, colorRGB, None)  # crée une image contenant du texte avec une certaine couleur
    textRect = text.get_rect()
    textRect.center = (0, 0)
    return text