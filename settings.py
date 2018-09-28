class Settings:
    # A class to store all settings for Pong
    def __init__(self):
        # Paddle settings
        self.paddle_speed = .5

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ball settings
        self.ball_radius = 20
        self.ball_color = (255, 255, 255)