class Settings():
    """ A Class to store all settings for alien invasion"""
    
    def __init__(self):
        # initializing the game's settings
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Backgraound color
        self.bg_color = (255,255,255)
        # Ship's Speed
        self.ship_speed_factor = 1.5