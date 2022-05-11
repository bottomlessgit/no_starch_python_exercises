from math import sqrt
class Settings():
    """
    The settings that dictate the arrangement
    and appearance of the stars in the sky
    """
    def __init__(self):
        """Initialize settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # Star settings
        self.image_link = "images/star.bmp"
        self.standard_size = 30
        self.min_size = 5
        self.max_size = 50
        self.standard_num_stars = 1000
        # Now set randomness settings
        self.random_rotation = True
        self.random_size = True
        # Set flags dealing with collisions 
        # And the possibility of running out of space
        self.forbid_collisions = True
        # Warning: forbiding space runout makes sky sparse of stars
        self.forbid_space_runout = False
        # Calculate max stars given collisions forbidden
        self.max_stars = self.calculate_max_stars()

    def calculate_max_stars(self):
        """Calcualte the maximum number of stars assuming max size,
        max rotation, and that in the worst case each star will have
        infinitessimally less space than a min star between each max-sized
        star in each direction"""
        # Max rotation increases size by a factor of sqrt(2)
        max_size_rotated = int(self.max_size * sqrt(2))
        min_size_rotated = int(self.min_size * sqrt(2))
        # Each star can have a stars worth of space between each neighbor
        space_per_star = max_size_rotated + min_size_rotated
        space_per_row = space_per_star
        min_stars_per_row = int(self.screen_width / space_per_star) - 1
        min_possible_rows = int(self.screen_height / space_per_row) - 1
        max_stars = min_stars_per_row * min_possible_rows
        return max_stars



