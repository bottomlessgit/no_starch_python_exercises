import sys
import pygame

def check_event(rocket):
        for event in pygame.event.get():
            # Respond to x-ing out window to quit
            if event.type == pygame.QUIT:
                sys.exit()
            # Respond to pressing of keys
            if event.type == pygame.KEYDOWN:
                process_keydown_event(event, rocket)
            # Respond to releasing of keys
            elif event.type == pygame.KEYUP: 
                process_keyup_event(event, rocket)

def process_keydown_event(event, rocket):
    """Sets movement flags for each direction based on keydown event"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def process_keyup_event(event, rocket):
    """Sets movement flags for each direction based on keyup event"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def update_screen(screen, rocket):
    """Draws next screen and flips screen to update"""
    screen.fill(rocket.rkt_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()




