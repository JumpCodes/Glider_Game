import pygame
from pygame.sprite import Sprite
import random

class Obstacle(Sprite):
    #Class to represent our obstacles the player will have to dodge.
    def __init__(self,hg_game):
        super().__init__()
        self.screen=hg_game.screen
        self.settings=hg_game.settings
        self.number=random.randint(1,3)
        white=(255,255,255)

        #Load our obstacle and get its rectangle
        image=pygame.image.load("alien.bmp")
        image=pygame.transform.scale(image,(50,50))
        image.set_colorkey(white)
        self.image=image
        self.rect=self.image.get_rect()

        if self.number == 1:
            #Start each new obstacle just off the very top of the screen
            self.x=random.randint(0, self.settings.screen_width-self.rect.width)
            self.y=0
            self.rect.x=self.x
            self.rect.y=self.y
        if self.number == 2:
            #Start each new obstacle at the left of the screen
            self.x=0
            self.y=random.randint(0,self.settings.screen_height)
            self.rect.x = self.x
            self.rect.y = self.y
        if self.number == 3:
            #Start each new obstacle at the right of the screen
            self.x=self.settings.screen_width-self.rect.width
            self.y=random.randint(0,self.settings.screen_height)
            self.rect.x = self.x
            self.rect.y = self.y

        #store the obstacles exact vertical location
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

    def update(self):
        if self.number == 1:
            #move the obstacle towards the bottom of the screen
            self.y+=self.settings.obstacle_speed
            self.rect.y=self.y
            self.rect.x=self.x
        if self.number == 2:
            # move the obstacle towards the bottom of the screen
            self.x += self.settings.obstacle_speed
            self.rect.y = self.y
            self.rect.x = self.x
        if self.number == 3:
            # move the obstacle towards the bottom of the screen
            self.x -= self.settings.obstacle_speed
            self.rect.y = self.y
            self.rect.x = self.x