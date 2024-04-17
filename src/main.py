try:
    import pygame
except ImportError:
    print("Pygame não está instalado. Instale-o com 'pip3 install pygame'")
    print("Confira o README.md para mais informações.")
    exit()

import player
import sys
import wall
import puff

# Inicializa o jogo
pygame.init()

# Configura o display
width = 800
height = 400
screen = pygame.display.set_mode((width, height))

# o jogador
p = player.Player(width, height)
w = wall.Wall(10, 10, 100, 100)
# criar um grupo de sprites para o jogador
group_player = pygame.sprite.Group()
group_player.add(p)

group_wall = pygame.sprite.Group()
largura_parede = 20
# Parede de cima
group_wall.add(wall.Wall(10, 10, width - largura_parede, largura_parede))
# Parede de baixo
group_wall.add(
    wall.Wall(10, height - largura_parede, width - largura_parede, largura_parede)
)
# Parede da esquerda
group_wall.add(wall.Wall(10, 10, largura_parede, height - largura_parede))
# Parede da direita
group_wall.add(
    wall.Wall(width - largura_parede, 10, largura_parede, height - largura_parede)
)

n_puffs = 10
for _ in range(n_puffs):
    group_wall.add(puff.Puff())

# Define a cor branco
white = (255, 255, 255)

# Cria um relógio
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white)  # pinta a tela de branco

    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed()
    colidiu = pygame.sprite.groupcollide(group_player, group_wall, False, False)
    p.move(keys, colidiu)
    group_player.draw(screen)
    group_wall.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
