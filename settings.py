class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initializes static game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens settings
        self.fleet_drop_speed = 10

        # Game acceleration rate.
        self.speedup_scale = 1.1
        # Alien value growth rate.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change during the game."""
        self.ship_speed = 3
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 indicates movement to the right; and -1 - to the left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed and rate settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
