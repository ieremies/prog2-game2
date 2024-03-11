
import pygame

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Cria uma imagem 50 x 50 e preenche com uma cor
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))

        # Define essa propriedade chamada mov_speed
        self.mov_speed = 5

        # Cria o rectângulo que representa ele, a image acima é só a visualização dele.
        self.rect = self.image.get_rect()               # pega as mesmas dimensões da imagem
        self.rect.center = (width // 2, height // 2)    # posição inicial do jogador

    def move(self, keys):
        """
        Altera a posição do jogador baseado nas teclas pressionadas.
        """
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.mov_speed
        if keys[pygame.K_s] and self.rect.bottom < height:
            self.rect.y += self.mov_speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.mov_speed
        if keys[pygame.K_d] and self.rect.right < width:
            self.rect.x += self.mov_speed