import pygame

class Mario():
    """ Mario game character to be printed to screen"""

    def __init__(self, screen):
        """Initialize mario and set it's starting position"""
        self.screen = screen

        #Load the Mario image and get it's rect
        big_mario = pygame.image.load('images/mario.bmp')
        self.image = pygame.transform.scale(big_mario, (60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set mario rect to the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw mario at his current location"""
        self.screen.blit(self.image, self.rect)