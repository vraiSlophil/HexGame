import pygame

from sprites.sprite_library import Images
from src.board import Board
from src.bot import Bot
from src.display import Screen, Button
from src.boxes import Box


def main():
    BOT_COLOR = -1

    # Initialisation de Pygame
    pygame.init()

    # Création du plateau de jeu
    board = Board(size=4)

    # Création du bot
    bot = Bot(board)

    # Création de l'écran
    screen = Screen(800, 600, board.get_board(), Images.HEXA0.value)

    # Création de l'horloge
    clock = pygame.time.Clock()

    # Création d'un bouton
    button1 = Button('Click me', 150, 40, (10, 400), 3, screen.get_screen())
    screen.add_button(button1)

    # Boucle principale du jeu
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Ajout de la détection du clic de souris
                pos_mouse = pygame.mouse.get_pos()
                for i in screen.get_box_sprite_group():
                    if i.rect.collidepoint(pos_mouse[0], pos_mouse[1]):  # Chercher s'il y a une collision avec les cases
                        if not board.is_finished(): # Ajout de la condition pour vérifier si le jeu est terminé
                            i.play()  # Jouer sur la case sur laquelle on a cliqué

                            # Mise à jour de l'état du jeu
                            board.update()

                # Si c'est le tour du bot, il joue
                if board.get_tour() == BOT_COLOR and not board.is_full():
                    bot.play()

        # Mise à jour de l'affichage
        screen.update()

        # Mise à jour de l'écran
        pygame.display.flip()

        clock.tick(60)

    # Quitter Pygame à la fin de la boucle
    pygame.quit()


if __name__ == "__main__":
    main()
