import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
line_points = [(10, 20), (20, 10), (30, 80), (900, 90), (40 ,30), (100 ,400), ]
line_color = (50, 60, 70)
pygame.draw.lines(screen, line_color, False, line_points, 5)
pygame.display.flip()

line_points_new = [(x + 50, y + 40) for x,y in line_points]
print(line_points_new)
pygame.draw.aalines(screen, line_color, False, line_points_new, 5)
pygame.display.flip()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()