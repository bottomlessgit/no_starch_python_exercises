import sys

import pygame

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1500, 900))

    bg_color = (16, 78, 139)

    # Start main loop of game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(bg_color)

            pygame.display.flip()

run_game()

