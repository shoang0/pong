import pygame
import sys
from paddles import Paddles
from ball import Ball


def check_keydown_events(event, pong_settings, screen, paddles):
    """Respond to key presses."""
    # Move paddles up, down, and quit
    if event.key == pygame.K_DOWN:
        paddles.moving_down = True
    elif event.key == pygame.K_UP:
        paddles.moving_up = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, pong_settings, screen, paddles):
    """Respond to key releases"""
    # Stop paddle movement when key is released
    if event.key == pygame.K_DOWN:
        paddles.moving_down = False
    elif event.key == pygame.K_UP:
        paddles.moving_up = False


def check_events(pong_settings, screen, stats, sb, play_button, paddles):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pong_settings, screen, paddles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pong_settings, screen, paddles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(pong_settings, screen, stats, sb, play_button, paddles, mouse_x, mouse_y)


def update_screen(pong_settings, screen, stats, sb, play_button, ball, paddles):
    # Update images on screen and flip to new screen
    # Redraw screen during each pass through the loop
    screen.fill(pong_settings.bg_color)

    # Draw paddles and ball
    paddles.blitme()
    ball.blitme()

    # Draw score information
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def check_play_button(pong_settings, screen, stats, sb, play_button, paddles, mouse_x, mouse_y):
    """Start a new game when player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()

        # Empty the list of paddles
        # paddles.empty()
        # balls.empty()
