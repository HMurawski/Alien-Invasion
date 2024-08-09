class Settings:
    """a class to store all settings for AI game"""
    def __init__(self):
        '''itilialize the game's settings:'''
        #screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (82,78,183)

        #ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        