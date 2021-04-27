class GameStats():
    """Tracking statistics for the game Alien Invasion."""

    def __init__(self, ai_game):
        """Initializes statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Alien Invasion launches with an active state.
        self.game_active = True

    def reset_stats(self):
        """Initializes statistics that change during the game."""
        self.ships_left = self.settings.ship_limit