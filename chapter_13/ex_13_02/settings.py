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
        self.star_width = 40
        self.star_height = 40
        # Star spacing settings as fraction of size
        self.x_spacing_factor = .7
        self.y_spacing_factor = .7

        # Composite information
        self.x_spacing = self.x_spacing_factor * self.star_width
        self.y_spacing = self.y_spacing_factor * self.star_height
        self.num_stars_in_row = int(self.screen_width / 
            (self.star_width + self.x_spacing))
        self.num_rows = int(self.screen_height / 
            (self.star_height + self.y_spacing))
        # Set edge space so that grid of stars is centered on screen
        self.edge_space_x = self.get_edge_space_x()
        self.edge_space_y = self.get_edge_space_y()

    def get_edge_space_x(self):
        total_star_width = self.star_width * self.num_stars_in_row
        total_space_width = self.x_spacing * (self.num_stars_in_row - 1)
        remaining_space = (self.screen_width - total_star_width 
        - total_space_width)
        x_distance_from_edge = .5 * remaining_space
        return x_distance_from_edge

    def get_edge_space_y(self):
        total_star_height = self.star_height * self.num_rows
        total_space_height = self.y_spacing * (self.num_rows - 1)
        remaining_space = (self.screen_height - total_star_height 
        - total_space_height)
        y_distance_from_edge = .5 * remaining_space
        return y_distance_from_edge
