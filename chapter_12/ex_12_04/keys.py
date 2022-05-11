import sys
import pygame

def run_game():
    """Runs empty window and runs loop to print keydown event values"""
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Keys")
    
    while True:
        pygame.display.flip()
        screen.fill((250, 250, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)

run_game()