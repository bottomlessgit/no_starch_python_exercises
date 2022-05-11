import sys
import pygame
from settings import Settings
from pygame.sprite import Group
from star import Star

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
    # Create and position stars
    create_stars(screen, ss_settings, stars)
    stars.draw(screen)
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def create_stars(screen, ss_settings, stars):
    """Creates and positions the fleet of stars in a centered grid"""
    for row in range(ss_settings.num_rows):
        for star_num in range(ss_settings.num_stars_in_row):
            new_star = Star(screen, ss_settings)
            new_star.rect.x = x_position(star_num, ss_settings)
            new_star.rect.y = y_position(row, ss_settings)
            stars.add(new_star)

def x_position(star_num, ss_settings):
    """Calculates x position given row and number star in row"""
    x_distance = (ss_settings.edge_space_x + 
        star_num * (ss_settings.star_width + ss_settings.x_spacing))
    return x_distance

def y_position(row, ss_settings):
    """Calculates x position given row and number star in row"""
    y_distance = (ss_settings.edge_space_y + 
        row * (ss_settings.star_height + ss_settings.y_spacing))
    return y_distance




starry_sky()