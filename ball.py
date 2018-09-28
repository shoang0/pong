import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """"A class to represent the pong ball"""

    def __init__(self, pong_settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.pong_settings = pong_settings

        # Load ball image and get its rect
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start ball at center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom / 2

    def blitme(self):
        """Draw the ball at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ball(self):
        self.center = self.screen_rect.centerx