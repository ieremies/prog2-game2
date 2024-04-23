# puff.py
"""
Classe que implementa um muro.
"""


import pygame
from random import choice


class Puff(pygame.sprite.Sprite):
    def __init__(self, width, height, lado_player):
        """
        Para ser criado, ele precisa da posição inicial, x e y, e das dimensões, width e height.
        """
        super().__init__()
        lado_puff = 40
        self.image = pygame.Surface((lado_puff, lado_puff))

        # Load asset wall
        self.image = pygame.image.load("img/puff.png")
        self.image = pygame.transform.scale(self.image, (lado_puff, lado_puff))

        # possibilidades de posicao (sem acertar o player)
        naoacertar_playerx = [
            _
            for _ in range(
                width // 2 - (lado_player + lado_puff),
                width // 2 + (lado_player + lado_puff),
            )
        ]
        possiveis_x = [
            x
            for x in range(
                lado_puff // 2 + 10, width - (lado_puff // 2 + 10), lado_puff + 5
            )
        ]
        for _ in possiveis_x:
            for i in naoacertar_playerx:
                if i == _:
                    possiveis_x.remove(i)

        naoacertar_playery = [
            _
            for _ in range(
                height // 2 - (lado_player + lado_puff),
                height // 2 + (lado_player + lado_puff),
            )
        ]
        possiveis_y = [
            y
            for y in range(
                lado_puff // 2 + 10, height - (lado_puff // 2 + 10), lado_puff + 5
            )
        ]
        for _ in possiveis_y:
            for i in naoacertar_playery:
                if i == _:
                    possiveis_y.remove(i)

        # combinações de x e y que podem ser usadas:
        possiveis_posicoes = [(x, y) for x in possiveis_x for y in possiveis_y]

        self.rect = self.image.get_rect()

        # Posiciona o muro na posição inicial
        self.rect.x, self.rect.y = choice(possiveis_posicoes)
        possiveis_posicoes.remove((self.rect.x, self.rect.y))
