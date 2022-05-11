import pygame

class Raindrop(pygame.sprite.Sprite):
    """Class to represent raindrop"""
    def __init__(self, qr_s, screen):
        """Create raindrop from settings and screen"""
        super().__init__()
        # Give raindrop screen to print to
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Load image and scale it
        self.image = pygame.image.load(qr_s.r_image_link)
        self.image = pygame.transform.scale(self.image, 
            (qr_s.r_width, qr_s.r_height))
        self.image = self.image.convert()
        # Get rectangle
        self.rect = self.image.get_rect()
        # Create precise value for y for precise fractional movement
        self.precise_y = float(self.rect.y)
        self.speed = qr_s.r_speed

    def past_bottom(self):
        """Returns true if top of raindrop passed bottom of screen"""
        return self.rect.top > self.screen_rect.bottom

    def update(self):
        """Updates position of raindrop"""
        self.precise_y += self.speed
        self.rect.y = self.precise_y
