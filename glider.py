import pygame

class Glider():

    def __init__(self,hg_game):
        #Initalize class
        super().__init__()
        self.screen = hg_game.screen
        self.settings=hg_game.settings
        self.screen_rect=hg_game.screen.get_rect()
        white=(255,255,255)

        #load the glider image
        image=pygame.image.load("SpaceShip.png")
        image=pygame.transform.scale(image,(25,25))
        image.set_colorkey(white)
        self.image=image
        self.rect=self.image.get_rect()

        #Start glider in center of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        self.y=self.rect.y
        self.x=self.rect.x

        # def movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        #draw glider in current location
        self.screen.blit(self.image,self.rect)

    def update(self):
        #Change movement flags and update ship location
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.glider_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.glider_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.glider_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.glider_speed
        self.rect.y=float(self.y)
        self.rect.x=float(self.x)

