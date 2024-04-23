##essas sao as missoes
import pygame

pygame.mixer.init()
som_descarga = pygame.mixer.Sound("sounds/descarga.wav")
som_lavarmao = pygame.mixer.Sound("sounds/washhands.wav")


class Missoes(pygame.sprite.Sprite):
    def __init__(self, tamanho, posicaox, posicaoy, rotacao):
        super().__init__()

        self.image = pygame.image.load("img/seta.png")
        self.image = pygame.transform.scale(self.image, (tamanho, tamanho // 2))
        pygame.transform.rotate(self.image, float(rotacao))

        # Define a hitbox da seta
        self.rect = self.image.get_rect()

        # Posiciona a seta
        self.rect.x = posicaox
        self.rect.y = posicaoy

    def fazermissao(self, tipo):
        if tipo == "lavarmao":
            som_lavarmao.play()
        if tipo == "descarga":
            som_descarga.play()
