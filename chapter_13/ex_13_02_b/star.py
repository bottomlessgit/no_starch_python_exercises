import pygame
from random import randint

class Star(pygame.sprite.Sprite):
    """Represents a star object"""
    def __init__(self, screen, ss_settings):
        """Initialize a star object"""
        # Initialize object as sprite
        super().__init__()
        # Load star image from images folder
        self.image = pygame.image.load(ss_settings.image_link)
        # If random_size flag active randomize size
        if ss_settings.random_size:
            rand_size = randint(ss_settings.min_size, ss_settings.max_size)
            self.image = pygame.transform.scale(self.image, 
                (rand_size, rand_size))
        else:
            self.image = pygame.transform.scale(self.image, 
                (ss_settings.standard_size, ss_settings.standard_size))
        # If random_rotation flag active, randomize rotation
        if ss_settings.random_rotation:
            """5 pointed rotationally symmetrical star means that
            1/5 of 360 degrees allows for all possible rotations"""
            rand_rotation = randint(0, 72)
            self.image = pygame.transform.rotate(self.image, rand_rotation)
        # Now randomize location on screen
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, ss_settings.screen_width - self.rect.width)
        self.rect.y = randint(0, ss_settings.screen_height - self.rect.height)

    def blitme(self, screen):
        screen.blit(self.image, self.rect)
        

