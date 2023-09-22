import sys
import pygame

from settings import Settings
from obstacles import Obstacle
from glider import Glider
from score import Score

class HangGlide:
    #This class will manage the overall game

    def __init__(self):
        #initialize the game
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.spawn_interval = self.settings.spawn_interval
        self.spawn_timer = self.settings.spawn_timer
        self.score=0

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Hang Glide")

        self.glider = Glider(self)
        self.sb = Score(self)

        self.obstacle=pygame.sprite.Group()
        self.circle=pygame.sprite.Group()

        self.create_obstacle()

    def run_game(self):
        #Start the main game loop
        while True:
            self.check_events()
            self.glider.update()
            self.sb.prep_score()
            self.update_screen()
            self.create_obstacle()
            self.update_obstacle()
            self.check_collisions()
            self.clock.tick(60)

    def check_events(self):
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        # Respond to key presses
        if event.key == pygame.K_RIGHT:
            # Move glider to the right
            self.glider.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move glider to the left
            self.glider.moving_left = True
        elif event.key == pygame.K_UP:
            # Move glider up
            self.glider.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move glider down
            self.glider.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit

    def check_keyup_events(self,event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.glider.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.glider.moving_left = False
        elif event.key == pygame.K_UP:
            self.glider.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.glider.moving_down = False

    def check_collisions(self):
        if pygame.sprite.spritecollideany(self.glider, self.obstacle):
            print("Your score is: "+str(self.sb.score))
            sys.exit()

    def update_screen(self):
        #Draw the screen each time we pass through the run game loop
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.image, (0,0))
        self.obstacle.draw(self.screen)
        self.glider.blitme()
        self.sb.show_score()
        # Make the screen visible
        pygame.display.flip()

    def create_obstacle(self):
        #Create an obstacle that travels in a straight line towards the player
        self.spawn_timer += pygame.time.get_ticks()
        if self.spawn_timer >= self.spawn_interval:
            obstacle=Obstacle(self)
            self.obstacle.add(obstacle)
            self.spawn_timer=0
            self.sb.score+=1

    def update_obstacle(self):
        #update the position of the obstacles
        self.obstacle.update()

if __name__ == "__main__":
    hg=HangGlide()
    hg.run_game()