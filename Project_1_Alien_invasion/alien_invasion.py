import pygame
from settings  import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def main():
    run_game()

def run_game():
    # initialize pygame, settings and a screen object
    pygame.init()
    
    # create a settings object
    ai_settings = Settings()
    
    screen = pygame.display.set_mode (
            (
            ai_settings.screen_width,
            ai_settings.screen_height
            )
        )
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets in.
    bullets = Group()
    
    # start the main loop for the game
    while True:
        
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        


main()
    
    