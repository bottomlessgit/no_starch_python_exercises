import pygame
from settings import Settings
import game_functions as gf
from rocket import Rocket

def run_game():
    # Initialize pygame
    pygame.init()

    rkt_settings = Settings()

    # Get screen object with desired size
    screen = pygame.display.set_mode(
        (rkt_settings.game_width, rkt_settings.game_height))
    screen_rect = screen.get_rect()

    # Create rocket instance
    rocket = Rocket(rkt_settings, screen)

    while True:
        # Respond to user input
        gf.check_event(rocket)
        # Update rocket position based on user input
        rocket.update()
        # Update screen and show to user
        gf.update_screen(screen, rocket)

run_game()




