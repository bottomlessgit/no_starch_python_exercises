import pygame

class Star(pygame.sprite.Sprite):
    """Represents a star object"""
    def __init__(self, screen, ss_settings):
        """Initialize a star object"""
        # Initialize object as sprite
        super().__init__()
        # Load star image from images folder
        self.image = pygame.image.load(ss_settings.image_link)
        self.image = pygame.transform.scale(self.image, 
            (ss_settings.star_width, ss_settings.star_height))
        self.rect = self.image.get_rect()

