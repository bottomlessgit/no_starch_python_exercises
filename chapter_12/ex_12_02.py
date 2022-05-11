import sys
import pygame
from mario import Mario

def run_game():
    pygame.init()
    screen = pygame.display.set_mode(1200,800)

    bg_color = (16, 78, 139)

    mario = Mario(screen)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(bg_color)
        mario.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()