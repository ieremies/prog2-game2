"""
Classe que implementa um banheiro
"""

import pygame


class Banheiro(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("img/schoolbathroom.png")
        self.rect = self.image.get_rect()  # mantem a escala da imagem
        self.rect.center = (0, 0)  # posição inicial do jogador
        self.image = pygame.transform.scale(
            self.image, (width, height)
        )  # arruma escala
