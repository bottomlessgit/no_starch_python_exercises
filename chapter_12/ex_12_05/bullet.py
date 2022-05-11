"""
Bullet class represents bullets that ship shoots
- Must have screen object to print to
- Must have settings to get size and color and speed
- Must have ship object to know starting location
Bullet
- Is created
- Has it's position moved (or is removed at a certain position)
- Is printed to screen
"""


import pygame

class Bullet(pygame.sprite.Sprite):
    """Class to represent bullet object that ship shoots"""
    def __init__(self, game_settings, screen, ship):
        super().__init__()
        """Initializes bullet at top of ship"""
        # Give bullet screen it prints to
        self.screen = screen
        # Create a rect of the correct size at (0, 0)
        self.rect = pygame.Rect(
           0, 0, game_settings.bullet_height, game_settings.bullet_width)
        # Set location to top center of chip
        self.rect.centery = ship.ship_rect.centery
        self.rect.right = ship.ship_rect.right
        # Create float value to represent x for decimal movement precision 
        self.precise_right = self.rect.right
        # Set speed and color from settings
        self.speed = game_settings.bullet_speed
        self.color = game_settings.bullet_color

    def update(self):
        """Updates bullet position"""
        # Change precise x value
        self.precise_right += self.speed
        # Set rect value to precise value
        self.rect.right = self.precise_right

    def blitme(self):
        """Draw the bullet to the game screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)




