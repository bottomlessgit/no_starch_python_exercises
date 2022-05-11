"""
Important Qualities of the ship:
- The surface onto which it is drawn
- The surface on which it is presented
- The image that displays the ship(from which its surface will be built)
- The rect that represents the ships position
- The x and y values of that rect
- The speed of the ship(from which it's)

What It Must Do:
# Move ship based on flags
# Print ship to game screen

"""


import pygame

class Ship():
    """Ship class that represents ship object"""
    def __init__(self, screen, game_settings):
        """Initializes Ship Object"""
        # Make surface from image file
        self.image = pygame.image.load('images/ship.bmp')
        # Transform image to size given in settings
        self.image = pygame.transform.scale(
            self.image, (game_settings.ship_width, game_settings.ship_height))
        # Rotate image so ship faces right
        self.image = pygame.transform.rotate(self.image, -90)
        self.ship_rect = self.image.get_rect()
        # Set game screen attribute for ship to access
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set initial position left edge center of screen
        self.ship_rect.centery = self.screen_rect.centery
        self.ship_rect.left = self.screen_rect.left
        # Create float representation of position for speed precision
        self.precise_centery = float(self.ship_rect.centery)
        # Set initial speed from game settings
        self.speed = game_settings.ship_speed
        # Set motion flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates position based on status of movement flags"""
        # Change float representation of center position based on movement flags
        if self.moving_up and self.ship_rect.top > self.screen_rect.top:
            self.precise_centery -= self.speed
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.precise_centery += self.speed
        # Update ships rect position based on precise float value
        self.ship_rect.centery = self.precise_centery

    def blitme(self):
        """Draws updated ship onto the main game screen"""
        self.screen.blit(self.image, self.ship_rect)





