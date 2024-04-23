"""
Classe que implementa um chao
"""

import pygame


class Chao(pygame.sprite.Sprite):
    def __init__(self, width, height):
        """
        Para ser criado, ele precisa da posição inicial, x e y, e das dimensões, width e height.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))

        # Load asset wall
        self.image = pygame.image.load("img/concreto.png")
        self.image = pygame.transform.scale(self.image, (width, height))

        # Define a hitbox do chao
        self.rect = self.image.get_rect()

        # canto esquerdo superior
        self.rect.x = 0
        self.rect.y = 0
