class GameStats():
    """Tracking statistics for the game Alien Invasion."""

    def __init__(self, ai_game):
        """Initializes statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #The record should not be reset.
        self.high_score = 0

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initializes statistics that change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1