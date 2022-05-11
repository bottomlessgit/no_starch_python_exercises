import pygame

class Rocket():
    """Represents controllable moving rocket in game"""

    def __init__(self, rkt_settings, screen):
        """Initiates vital attributes of ship"""

        # Set settings object for access to relevant ship settings
        self.rkt_settings = rkt_settings

        # Set screens and rocket screens for printing and controlling position
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rocket_image = pygame.image.load("images/rocket.bmp")
        self.rocket_rect = self.rocket_image.get_rect()

        # Set initial position of rocket
        self.rocket_rect.centerx = self.screen_rect.centerx
        self.rocket_rect.centery = self.screen_rect.centery

        # Set moving flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Create float values to represent rocket position for precision
        self.rocket_center_x = float(self.rocket_rect.centerx)
        self.rocket_center_y = float(self.rocket_rect.centery)

    def update(self):
        """Update the position of the Rocket"""
        # Update x and y positions based on movement flags
        if (self.moving_right and 
                self.rocket_rect.right < self.screen_rect.right):
            self.rocket_center_x += self.rkt_settings.rocket_speed_x
        if (self.moving_left and 
                self.rocket_rect.left > self.screen_rect.left):
            self.rocket_center_x -= self.rkt_settings.rocket_speed_x
        if (self.moving_up and 
                self.rocket_rect.top > self.screen_rect.top):
            self.rocket_center_y -= self.rkt_settings.rocket_speed_y
        if (self.moving_down and 
                self.rocket_rect.bottom < self.screen_rect.bottom):
            self.rocket_center_y += self.rkt_settings.rocket_speed_y
        # Assign integer position values of rocket using updated float values
        self.rocket_rect.centerx = self.rocket_center_x
        self.rocket_rect.centery = self.rocket_center_y

    def blitme(self):
        """Draw Rocket to screen"""
        self.screen.blit(self.rocket_image, self.rocket_rect)




