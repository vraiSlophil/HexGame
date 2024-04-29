import pygame

from sprites.sprite_library import Images

pygame.init()


# Cette fonction a été majoritairement faite par Gabin et Nathan O a aidé et bidouillé quelques fois

# classe écran
class Screen:
    def __init__(self, width, height, list_boxes, img_hex):
        self.__width = width  # largeur de l'écran
        self.__height = height  # hauteur de l'écran
        self.__screen = pygame.display.set_mode((self.__width, self.__height))  # création de l'affichage
        self.__globalfont = pygame.font.SysFont(None, 16)  # on charge la police d'écriture, on pourra changer
        pygame.display.set_caption("Hex game")  # juste un titre pour la fenêtre

        self.__button_group = []  # on crée un groupe de boutons

        self.__imgsize = 64  # taille de l'image en pixels
        self.__img_hex = Images.HEXA0.value  # on charge l'image de l'hexagone
        self.list_boxes = list_boxes  # la liste des instances boxes
        self.__box_sprite_group = pygame.sprite.Group()  # on fait des groupes de sprites pour les update
        self.__elements_group = pygame.sprite.Group()  # plus facilement

        for box_instance in self.list_boxes.values():  # on relie chaque instance box avec une instance de sprite
            sprite_box = BoxSprite(box_instance, self.__img_hex, self.__imgsize)
            self.__box_sprite_group.add(sprite_box)

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

        for button in self.__button_group:
            button.draw()

    def add_button(self, button):
        self.__button_group.append(button)


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
        self.rect.x = (x * imgsize) + (imgsize / 2 * y) + (imgsize / 8 * y) + (imgsize / 4 * x) + 15
        self.rect.y = (y * imgsize) + 15
        self.img_size = imgsize

    def play(self):
        self.box_instance.play()

    def update(self):
        color = self.box_instance.get_color()  # on change la case de couleur en fonction de la valeur de son instance
        if color == 1:  # non-graphique
            self.image = Images.HEXA1.value
            self.image = pygame.transform.scale(self.image, (self.img_size, self.img_size))
        elif color == 0:
            self.image = Images.HEXA0.value
            self.image = pygame.transform.scale(self.image, (self.img_size, self.img_size))
        else:
            self.image = Images.HEXA_1.value
            self.image = pygame.transform.scale(self.image, (self.img_size, self.img_size))


class Button:
    def __init__(self, text, width, height, pos, elevation, screen):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.screen = screen

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'

        #text
        self.text_surf = pygame.font.Font(None, 30).render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=12)
        self.screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    print('click')
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'
