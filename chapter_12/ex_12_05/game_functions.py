import sys
import pygame
from bullet import Bullet

def check_events(ship, bullets, game_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, game_settings, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship, bullets, game_settings, screen):
    """Responds to different keydown events"""
    if event.key == pygame.K_SPACE:
        fire_bullet(ship, bullets, game_settings, screen)
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True

def check_keyup_events(event, ship):
    """Responds to different keyop events"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def fire_bullet(ship, bullets, game_settings, screen):
    # Create new bullet above center of where ship is
    # And add that bullet to the group of bullets
    # Need bullet group to add the new bullet to the bullet group
    # Need settings for size and color (and to limit number of bullets)
    # Need ship to find location to put bullet
    # Need screen object to print the bullet to the screen
    if len(bullets) < game_settings.max_bullets:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def update_objects(ship, bullets, game_settings):
    """Move ship and bullets according to their settings"""
    ship.update()
    bullets.update()
    for bullet in bullets:
        if bullet.rect.right >= game_settings.screen_width:
            bullets.remove(bullet)

def print_screen(ship, bullets, screen, game_settings):
    screen.fill(game_settings.bg_color)
    ship.blitme()
    for bullet in bullets:
        bullet.blitme()
    pygame.display.flip()





