import pygame
import math
from random import randrange
from pygame.sprite import Sprite


class Ball(Sprite):
    """"A class to represent the pong ball"""

    def __init__(self, pos, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load ball image and get its rect
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (15, 15), 15)
        self.rect = self.image.get_rect()

        # Start ball at center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom / 2

        # Store ball position as decimal value
        self.x = float(self.rect.x)
        self.speed_factor = .5

        # Create a vector with random angle
        # self.rect = self.image.get_rect(center=pos)
        # self.vel = pygame.math.Vector2(7, 0).rotate(randrange(360))
        # self.pos = pygame.math.Vector2(pos)

    def blitme(self):
        """Draw the ball at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ball(self):
        self.center = self.screen_rect.centerx

    # def update(self):
        # self.pos += self.vel
        # self.rect.center = self.pos

    def update(self):
        # sideways test
        self.x -= self.speed_factor
        self.rect.x = self.x