"""
Classe que implementa um muro.
"""

import pygame
from random import choice

possiveis_x = [x for x in range(50,750, 40)]
possiveis_y = [x for x in range(50,350, 40)]

class Puff(pygame.sprite.Sprite):
    def __init__(self):
        """
        Para ser criado, ele precisa da posição inicial, x e y, e das dimensões, width e height.
        """
        super().__init__()
        lado_puff = 40
        self.image = pygame.Surface((lado_puff, lado_puff))

        # Load asset wall
        self.image = pygame.image.load("img/puff.png")
        self.image = pygame.transform.scale(self.image, (lado_puff, lado_puff))

        # Define a hitbox do muro
        self.rect = self.image.get_rect()

        # Posiciona o muro na posição inicial

        self.rect.x = choice(possiveis_x)
        possiveis_x.remove(self.rect.x)
        self.rect.y = choice(possiveis_y)
        possiveis_y.remove(self.rect.y)
