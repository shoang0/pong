import pygame
from pygame.sprite import Group
from settings import Settings
from paddles import Paddles
from scoreboard import Scoreboard
from game_stats import GameStats
from button import Button
from ball import Ball
import game_functions as gf


def run_game():
    # Initialize pygame, settings,
    pygame.init()
    pong_settings = Settings()
    screen = pygame.display.set_mode((pong_settings.screen_width, pong_settings.screen_height))
    ball = Ball(pong_settings, screen)
    pygame.display.set_caption("Pong")

    # Make the play button
    play_button = Button(pong_settings, screen, "Play")

    # Create an instance to score stats and create scoreboard
    stats = GameStats(pong_settings)
    sb = Scoreboard(pong_settings, screen, stats)

    # Make the paddles and ball
    paddles = Paddles(pong_settings, screen)

    while True:
        gf.check_events(pong_settings, screen, stats, sb, play_button, paddles)
        # pygame.display.set_caption("Work")
        if stats.game_active:
            paddles.update()
            ball.update()

        gf.update_screen(pong_settings, screen, stats, sb, play_button, ball, paddles)


run_game()
