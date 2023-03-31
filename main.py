import pygame
from pygame import QUIT

from src.board import Board
from src.bot import Bot
from src.database import Database
from src.display import Screen, Button
from sprites.sprite_library import hexa0

pygame.init()

img_hex_void = hexa0

board = Board()
screen = Screen(800, 500, board.get_board(), img_hex_void)
database = Database()
bot = Bot(board, database)


# Joueur bleu = True et de couleur 1, joueur rouge = False et de couleur -1
marche = True  # pour gérer la boucle de l'affichage
tour = True
fini = False

clock = pygame.time.Clock()
fps = 30
tick = 0
lastmousepos = 0  # pour stocker si on maintient un click (0 pour non, 1 pour oui)
coords_blue = []


def get_mouse_click_rect(souris):  # détecte le rectangle sur lequel on a cliqué avec la souris
    if souris[0] == 1 and lastmousepos == 0:  # on vérifie si on a pas clické trop récemment
        pos_mouse = pygame.mouse.get_pos()
        for i in screen.get_elements_group():
            if i.rect.collidepoint(pos_mouse[0], pos_mouse[1]):  # chercher s'il y a une collision avec les rectangles
                return i  # retourne l'instance sur laquelle on a cliqué avec la souris
        for i in screen.get_box_sprite_group():
            if i.rect.collidepoint(pos_mouse[0], pos_mouse[1]):  # chercher s'il y a une collision avec les cases
                return i


def jeu():
    while not fini:
        if tour:
            pass
        else:
            pass


def get_database():
    return database


# for box_instance in board.get_board().values():
#     box_instance.set_color(1)

while marche:
    events = pygame.event.get()
    touches = pygame.key.get_pressed()
    souris = pygame.mouse.get_pressed()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                marche = False
        if e.type == QUIT:
            pygame.quit()


    get_click = get_mouse_click_rect(souris)
    lastmousepos = souris[0]
    if get_click != None:
        get_click.play()
    for i in screen.get_elements_group():
        if type(i) == Button and i.category == 'counter':
            i.edit_text(str(tick))
    screen.update()
    pygame.display.update()  # on met à jour l'affichage
    tick += 1


    clock.tick(fps)  # pour que la boucle n'aille pas trop vite (limitée à 30 millièmes de seconde)
