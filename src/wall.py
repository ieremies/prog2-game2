"""
Classe que implementa um muro.
"""

import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """
        Para ser criado, ele precisa da posição inicial, x e y, e das dimensões, width e height.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))

        # Load asset wall
        self.image = pygame.image.load("img/wall.png")
        self.image = pygame.transform.scale(self.image, (width, height))

        # Define a hitbox do muro
        self.rect = self.image.get_rect()

        # Posiciona o muro na posição inicial
        self.rect.x = x
        self.rect.y = y
