class GameStats:
    '''track statistics for Alien Invasion'''

    def __init__(self, ai_game):
        '''initialize statistics'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        self.level = 1
        self.high_score = 0

        #Start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ship_left = self.settings.ship_limit