import pygame
from pygame.sprite import Sprite


class Paddles(Sprite):
    def __init__(self, pong_settings, screen):
        super(Paddles, self).__init__()
        self.screen = screen
        self.pong_settings = pong_settings

        # Create paddle1
        self.image = pygame.image.load('images/paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # center of screen
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the paddle's center
        self.center = float(self.rect.y)

        # Movement flag
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the paddle's position based on movement flag"""
        # Update paddle's center value, not the rectangle
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.pong_settings.paddle_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.pong_settings.paddle_speed

        self.rect.centery = self.center

    def center_paddle(self):
        """Center the paddle on the screen"""
        self.center = self.screen_rect.centerx

    def blitme(self):
        # draw at loc
        self.screen.blit(self.image, self.rect)
