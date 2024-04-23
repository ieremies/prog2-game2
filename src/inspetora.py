# inspetora
import pygame


# definir a classe inspetora
class Inspetora(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # parâmetros de posição e movimento
        self.x = x
        self.y = y
        # TODO fotinha
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 140, 0))
        # Cria o rectângulo
        self.rect = self.image.get_rect()  # pega as mesmas dimensões da imagem
        self.rect.center = (x, y)  # posição inicial do jogador
        self.velocidade = 3

    # função de perseguição do jogador
    def perseguir(self, diferenca_x, diferenca_y, dificuldade):
        # isso é pro ajuste de dificuldade, ta escrito (dificuldade - 1) para que quando a dificuldade
        # for 1 ela não afetar o valor original da self.velocidade
        self.velocidade = self.velocidade + (dificuldade - 1) * 0.3

        # isso é pra mudar a posição da inspetora
        if diferenca_x >= 0:
            self.rect.x += self.velocidade

        elif diferenca_x < 0:
            self.rect.x -= self.velocidade

        if diferenca_y >= 0:
            self.rect.y += self.velocidade
        elif diferenca_y < 0:
            self.rect.y -= self.velocidade
