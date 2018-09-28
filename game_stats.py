class GameStats:
    """Track stats for Pong"""

    def __init__(self, pong_settings):
        self.pong_settings = pong_settings
        self.reset_stats()

        # Start Pong in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.p1score = 0
        self.p2score = 0