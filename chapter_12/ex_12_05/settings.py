"""
Relevant Settings:
-


"""


import pygame

class Settings():
    """A class for organizing relevant changeable game settings"""
    def __init__(self):
        """Initialize game settings"""
        # Settings of Background Screen
        self.bg_color = (255, 255, 255)
        self.screen_width = 800
        self.screen_height = 800
        # Ship settings
        self.ship_image_path = 'images/ship.bmp'
        self.ship_speed = 1
        self.ship_width = 60
        self.ship_height = 50
        # Bullet settings
        self.bullet_color = (5, 5, 5)
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 9
        self.max_bullets = 4

