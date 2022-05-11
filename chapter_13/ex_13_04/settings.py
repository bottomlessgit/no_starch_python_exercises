"""
Print raindrops to screen then have them fall and dissappear
when they hit the bottom of the screen.
Required settings for screen:
-Width
-Height
-Background color

Required settings for raindrop:
image chosen(so filepath to image)
- Width
- Height
- Arrangement: 
    Distance between x
    Distance between y
    resulting amount fitting in row
    number of rows fitting on screen
    Ramining distance between drops and edge of screen for centering



"""


import pygame

class Settings():
    """Settings to control screen and rain settings"""
    def __init__(self):
        # Screen size
        self.s_width = 1200
        self.s_height = 800
        # Screen color
        self.bg_color = (0, 0, 0)
        # Rain image link
        self.r_image_link = "images/small_raindrop.png"
        # Rain size
        self.r_width = 30
        self.r_height = 40
        # Rain speed
        self.r_speed = 1
        # Spacing between raindrops as fraction of ranindrop size
        self.x_dist_factor = .5
        self.y_dist_factor = .5
        # Spacing between raindrops
        self.x_dist = self.x_dist_factor * self.r_width
        self.y_dist = self.y_dist_factor * self.r_height
        # Number of aliens in a row and number of rows
        self.num_r_in_row = int(self.s_width / (self.r_width + self.x_dist))
        self.num_rows = int(self.s_height / (self.r_height + self.y_dist)) + 2
        # Calculate height at which you replace raindrop for continuous effect
        self.replacement_height = (self.s_height - 
            (self.num_rows * (self.y_dist + self.r_height)))
      



