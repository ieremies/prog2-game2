# classe implementa estrelitos
import pygame

import random  # para gerar os numeros aleatorios


class Estrelitos(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.image.load("img/estrelito.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

        # Define a hitbox do estrelito
        self.rect = self.image.get_rect()

        # Posiciona o estrelito aleatoriamente
        self.rect.x = random.randint(
            15, width - 50
        )  # cuidado com a espessura das paredes e com o tamanho do estrelito
        self.rect.y = random.randint(15, height - 50)
