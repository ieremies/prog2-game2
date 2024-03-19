import pygame

class Labirinto(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()

        # Cria uma imagem 50 x 50 e preenche com uma cor
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))

        # Define essa propriedade chamada mov_speed
        self.mov_speed = 5

        # Cria o rectângulo que representa ele, a image acima é só a visualização dele.
        self.rect = self.image.get_rect()               # pega as mesmas dimensões da imagem
        self.rect.center = (width // 2, height // 2)    # posição inicial do jogador

        self.width = width
        self.height = height
