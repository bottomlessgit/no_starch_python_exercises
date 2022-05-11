"""
Aspects of Game:
Screen:
-Background
-Caption
-Quitting option
Ship
-Moves Up and Down
-Has specific speed
-Needs its own rectangle
-Moves only within bounds of screen
-Shoots bullets
Bullets:
- Moves to the right
- Is created and shot by ship
- Starts at ship location
- Dissappears when reaching end of screen
- Has a specific speed
- Has a color and size


We must initialize:
- A screen to print everything to
- A ship with all the ship attributes
- A group to keep track of all the bullets

Every frame must:
- Print the Background screen
- Respond to input to move the ship
- Print the Ship at new position
- Respond to input to shoot bullets
- Create a bullet in response
- move all bullets and print them all

Files to have:
A main file to run everything
A ship file(and class) to handle attributes of ship and to handle moving and printing of ship
A bullet file(and class) to handle bullet attributes and bullet movement
A settings(and class for passing) file to keep track of general game settings that it'd be convenient to easily change
A file for responding to input and refactoring behaviors, should do the majority of the work of the program

External Modules Required:
pygame
sys for exiting
"""
import sys
import pygame
from settings import Settings
from pygame.sprite import Group
import game_functions as gf
from ship import Ship

def run_game():
    # Initialize pygame
    pygame.init()
    # Initialize game settings object
    game_settings = Settings()
    # Initialize display screen
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")
    screen.fill(game_settings.bg_color)
    # Initialize ship
    ship = Ship(screen, game_settings)
    # Initialize bullet group
    bullets = Group()

    # Start loop
    while True:
        gf.check_events(ship, bullets, game_settings, screen)
        gf.update_objects(ship, bullets, game_settings)
        gf.print_screen(ship, bullets, screen, game_settings)

run_game()





