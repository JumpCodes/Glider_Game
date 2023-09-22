import pygame

#A class to store any game settings

class Settings:

    def __init__(self):

        #Screen Settings
        self.screen_width=500
        self.screen_height=600
        self.bg_color=(155,155,155)
        image=pygame.image.load("space.png")
        image=pygame.transform.scale(image,(self.screen_width, self.screen_height))
        self.image=image

        #Obstacle Settings
        self.obstacle_speed=1.0

        #Spawn Characteristics
        self.spawn_interval=1000000
        self.spawn_timer=0

        #glider characteristics
        self.glider_speed = 2.0
