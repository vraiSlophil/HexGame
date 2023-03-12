import pygame
from pygame import K_ESCAPE, QUIT
from sprites.sprite_library import hexa0

from clazz.board import Board
from clazz.database import Database
from clazz.display import Screen

pygame.init()

img_hex_void = hexa0

screen = Screen(600, 300, [], img_hex_void)
board = Board()
# database = Database()
# Joueur bleu = True et de couleur 1, joueur rouge = False et de couleur -1
marche = True  # pour gérer la boucle de l'affichage
tour = True
fini = False
clock = pygame.time.Clock()
fps = 30
coords_blue = []


def get_mouse_click_rect(souris):  # détecte le rectangle sur lequel on a cliqué avec la souris
    if souris[0] == 1:
        pos_mouse = pygame.mouse.get_pos()
        print(pos_mouse)
        for i in screen.elements_group:
            if i.rect.collidepoint(pos_mouse[0], pos_mouse[1]):  # chercher s'il y a une collision avec les rectangles
                return i  # retourne l'instance sur laquelle on a cliqué avec la souris
        for i in screen.box_sprite_group:
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


while marche:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                marche = False
        if e.type == QUIT:
            pygame.quit()
    touches = pygame.key.get_pressed()
    souris = pygame.mouse.get_pressed()

    screen.update()
    pygame.display.update()  # on met à jour l'affichage
    clock.tick(fps)  # pour que la boucle n'aille pas trop vite (limitée à 30 millièmes de seconde)
