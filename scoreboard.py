import pygame.font
from pygame.sprite import Group
from paddles import Paddles

class Scoreboard:
    """A class to keep track of score"""
    def __init__(self, pong_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pong_settings = pong_settings
        self.stats = stats

        # Font settings for score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        p1score = round(self.stats.p1score, -1)
        p2score = round(self.stats.p2score, -1)
        p1score_str = "{}".format(p1score)
        p2score_str = "{}".format(p2score)
        self.p1score_image = self.font.render(p1score_str, True, self.text_color, self.pong_settings.bg_color)
        self.p2score_image = self.font.render(p2score_str, True, self.text_color, self.pong_settings.bg_color)

        # Display the score at the top of the screen
        self.p1score_rect = self.p1score_image.get_rect()
        self.p2score_rect = self.p2score_image.get_rect()
        self.p1score_rect.right = self.screen_rect.right - 300
        self.p1score_rect.top = 20

        self.p2score_rect.left = self.screen_rect.left + 300
        self.p2score_rect.top = 20

    def show_score(self):
        """Draw scores to screen"""
        self.screen.blit(self.p1score_image, self.p1score_rect)
        self.screen.blit(self.p2score_image, self.p2score_rect)