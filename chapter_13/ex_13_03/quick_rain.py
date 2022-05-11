import sys
import pygame
from settings import Settings
from pygame.sprite import Group
from raindrop import Raindrop

def quick_rain():
    # Initialize pygame libraries
    pygame.init()

    # Initialize settings object
    qr_s = Settings()

    # Initialize screen object
    screen = pygame.display.set_mode((qr_s.s_width, qr_s.s_height))

    # Create sprite group for raindrops
    raindrops = Group()

    create_raindrops(qr_s, screen, raindrops)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        update_raindrops(qr_s, raindrops)
        draw_screen(qr_s, screen, raindrops)



def create_raindrops(qr_s, screen, raindrops):
    """Creates raindrops positions them and adds them to Group"""
    for drop_num in range(qr_s.num_r_in_row):
        for row_num in range(qr_s.num_rows):
            new_raindrop = createraindrop(qr_s, screen, drop_num, row_num)
            raindrops.add(new_raindrop)

def createraindrop(qr_s, screen, drop_num, row_num):
    """Creates a single raindrop in the desired position"""
    # Create Raindrop
    new_raindrop = Raindrop(qr_s, screen)
    new_raindrop.rect.x = (qr_s.x_edge_dist + 
        drop_num * (qr_s.r_width + qr_s.x_dist))
    new_raindrop.rect.y = (qr_s.y_edge_dist + 
        row_num * (qr_s.r_height + qr_s.y_dist))
    new_raindrop.precise_y = new_raindrop.rect.y
    return new_raindrop

def update_raindrops(qr_s, raindrops):
    raindrops.update()
    for raindrop in raindrops:
        if raindrop.past_bottom():
            raindrops.remove(raindrop)

def draw_screen(qr_s, screen, raindrops):
    screen.fill(qr_s.bg_color)
    raindrops.draw(screen)
    pygame.display.flip()

quick_rain()

