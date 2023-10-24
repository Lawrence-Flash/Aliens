The Alien Invasion game written in Python programming Language
The Following file Descibe the How The Game is Programmed

1. alien_invasion.py
    The main file, alein_invasion.py, creates a number of impoertant objects used throughout the game: the settings are stored in ai_settings, the main display surface is stored in screen, and a ship instance is created in this file as well. also stored in the alien_invasion.py is the maini loop of the game, which is a while loop that calls check_events(), ship.update(), and update_screen().
    alien_invasion.py is the only file you need to run when you want to play the Alien Invasion. The other files - settings.py, game_functions.py, ship.py: contain code that is imported, directly or indirectly, into this file

2. setting.py
    The settigs.py file contains the settings class. This class only has an __init__() method, which initializes attibutes controlling the game's appearence and ship's speed.
    then this file also includes the values needed for new bullet class
    these settings create blue bullets with a width of 3 pixels and a height of 15 pixels

3. game_functions.py
    The game_functions.py file contains a number of functions that carry out the bulk of the work in the game. The check_events() function detects relevant events, such as keyprersses and releases, and processes each of these types of events though the helper functions check_keydown_events() and check_keyup_events(). for now, these functions manage the movement of the ship. The game_functions modeule also contains update_screen(), which redraws the screen on each pass through the main loop.

4. ship.py
    The ship.py file contains the Ship class. Ship has an __init__() method, an
    update() method to manage the ship’s position, and a blitme() method
    to draw the ship to the screen. The actual image of the ship is stored in
    ship.bmp, which is in the images folder

5. bullet.py
    the Bullet class inherits from Sprite, which i imported from the pygame.sprite module. when you use sprites, you can group related elements in your game and act on all the grouped elements at once.
