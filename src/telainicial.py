import pygame


class TelaInicial(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("img/logoelite.png")
        self.rect = self.image.get_rect()  # mantem a escala da imagem
        self.rect.center = (width / 2, height / 2)  # posição inicial do jogador
