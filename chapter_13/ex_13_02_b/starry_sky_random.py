import sys
import pygame
from settings import Settings
from pygame.sprite import Group
from star import Star
from random import randint

def starry_sky():
    """Function that prints stars to black screen in a grid"""
    pygame.init()
    ss_settings = Settings()
    # Create display screen surface
    screen = pygame.display.set_mode((ss_settings.screen_width, 
        ss_settings.screen_height))
    screen.fill(ss_settings.bg_color)
    # make group to keep track of all stars
    stars = Group()
    # Check number of stars is allowed
    if (ss_settings.forbid_space_runout and 
        ss_settings.forbid_collisions and (ss_settings.standard_num_stars >
            ss_settings.max_stars)):
        num_stars = ss_settings.max_stars
    else:
        num_stars = ss_settings.standard_num_stars

    pygame.display.flip()
    # For some reason no display until program is queried for events
    pygame.event.get()

    # Create and position stars
    create_stars(num_stars, stars, screen, ss_settings)
    #stars.draw(screen)
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def create_stars(num_stars, stars, screen, ss_settings):
    num_stars_created = 0
    while num_stars_created < num_stars:
        new_star = Star(screen, ss_settings)
        if ss_settings.forbid_collisions:
            if not pygame.sprite.spritecollide(new_star, stars, False):
                stars.add(new_star)
                num_stars_created += 1
                new_star.blitme(screen)
                pygame.display.flip()

        else:
            stars.add(new_star)
            num_stars_created += 1
            new_star.blitme(screen)
            pygame.display.flip()





starry_sky()