import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """The class for controlling the projectiles fired by the ship."""

    def __init__(self, ai_game):
        """Creates a projectile object at the current position of the ship."""
        super(Bullet, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a projectile at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The position of the projectile is stored in real format.
        self.y = float(self.rect.y)
    
    def update(self):
        """Moves the bullet up the screen."""
        # Updating the position of the projectile in real format.
        self.y -= self.settings.bullet_speed
        # Updating the position of the rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Bullet output to the top of the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
