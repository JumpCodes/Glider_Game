import pygame.font

class Score():
    #A class to report scoring information
    def __init__(self,hg_game):
        #Initialize scorekeeping attributes
        self.hg_game=hg_game
        self.screen=hg_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=hg_game.settings
        self.score=hg_game.score

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

    def prep_score(self):
        #Turn the score into a rendered image
        score_str=f"{self.score:,}"
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        #Display score at top right of screen
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        #Draw score, level, and ships to the screen
        self.screen.blit(self.score_image,self.score_rect)


