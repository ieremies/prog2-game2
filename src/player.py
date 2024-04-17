import pygame
pygame.mixer.init()
musica_de_colisao_com_a_belissima_parede = pygame.mixer.Sound("OLe.wav")
musica_de_colisao_com_a_belissima_parede.set_volume(1000.0)

musica_de_dor_belissima = pygame.mixer.Sound("AAAA.wav")

# Define Player class
# 
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        # Cria uma imagem 50 x 50 e preenche com uma cor
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 128, 255))

        # Define essa propriedade chamada mov_speed
        self.mov_speed = 5

        # Cria o rectângulo que representa ele, a image acima é só a visualização dele.
        self.rect = self.image.get_rect()               # pega as mesmas dimensões da imagem
        self.rect.center = (width // 2, height // 2)    # posição inicial do jogador

        self.width = width
        self.height = height

        self.oldx = self.rect.centerx
        self.oldy = self.rect.centery

        self.som_tocando = pygame.mixer.get_busy()

    def move(self, keys, colidiu):
        """
        Altera a posição do jogador baseado nas teclas pressionadas.
        """
        self.som_tocando = pygame.mixer.get_busy()
        
        if not colidiu:
            if (self.rect.centerx == self.oldx) and (self.rect.centery == self.oldy):
                musica_de_colisao_com_a_belissima_parede.stop()

            print(self.oldx)
            print(self.rect.centerx)

            self.oldx = self.rect.centerx
            self.oldy = self.rect.centery

            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.mov_speed
            if keys[pygame.K_s] and self.rect.bottom < self.height:
                self.rect.y += self.mov_speed
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.mov_speed
            if keys[pygame.K_d] and self.rect.right < self.width:
                self.rect.x += self.mov_speed

            if not self.som_tocando:
                musica_de_colisao_com_a_belissima_parede.play()

                
            
        else:
            self.rect.centerx = self.oldx
            self.rect.centery = self.oldy

            if not self.som_tocando:
                musica_de_dor_belissima.play()
        
