import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''class to represent a single alien in the fleet'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #load the alien image and set its rectangle attributes
        self.image = pygame.image.load("images\\alien.bmp")
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alient's exact horizontal position
        self.x = float(self.rect.x)