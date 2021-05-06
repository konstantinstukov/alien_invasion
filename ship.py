import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving the real coordinate of the center of the ship
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        # move flag
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def update(self):
        """Updates the ship's position with the flag."""
        # The x attribute is updated, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # if self.moving_up and self.rect.top > 0:
        #     self.y -= self.settings.ship_speed
        # if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # self.y += self.settings.ship_speed

        # Updating the rect attribute based on self.x
        self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places the ship in the center of the lower side."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
