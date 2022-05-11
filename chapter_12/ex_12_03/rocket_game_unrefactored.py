import sys
import pygame


def run_game():
    # Initialize pygame
    pygame.init()

    bg_color = (255, 255, 255)

    # Get screen object with desired size
    screen = pygame.display.set_mode((800, 800))
    screen_rect = screen.get_rect()

    rocket_image = pygame.image.load("images/rocket.bmp")
    rocket_rect = rocket_image.get_rect()
    
    # Set initial possition of rocket
    rocket_rect.centerx = screen_rect.centerx
    rocket_rect.centery = screen_rect.centery

    # Set moving flags
    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    # Create float values to represent rocket position for precision
    rocket_center_x = float(rocket_rect.centerx)
    rocket_center_y = float(rocket_rect.centery)

    # Set rocket x-axis and y-axis movement speed factors
    rocket_speedx = 1.5
    rocket_speedy = 1.5


    while True:
        for event in pygame.event.get():
            # Respond to x-ing out window to quit
            if event.type == pygame.QUIT:
                sys.exit()
            # Respond to pressing of keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True
            # Respond to releasing of keys
            elif event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_DOWN:
                    moving_down = False

        if moving_right and rocket_rect.right < screen_rect.right:
            rocket_center_x += rocket_speedx
        if moving_left and rocket_rect.left > screen_rect.left:
            rocket_center_x -= rocket_speedx
        if moving_up and rocket_rect.top > screen_rect.top:
            rocket_center_y -= rocket_speedy
        if moving_down and rocket_rect.bottom < screen_rect.bottom:
            rocket_center_y += rocket_speedy

        rocket_rect.centerx = rocket_center_x
        rocket_rect.centery = rocket_center_y



        screen.fill(bg_color)
        screen.blit(rocket_image, rocket_rect)


        pygame.display.flip()



run_game()




