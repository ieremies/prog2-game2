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
group_wall.add(wall.Wall(10, 10, width-largura_parede, largura_parede))
group_wall.add(wall.Wall(10, height-largura_parede, width-largura_parede, largura_parede))
group_wall.add(wall.Wall(10, 10, largura_parede, height-largura_parede))
group_wall.add(wall.Wall(width-largura_parede, 10, largura_parede, height-largura_parede))
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())
group_wall.add(puff.Puff())

# Define a cor branco
white = (255, 255, 255)

# Cria um relógio
clock = pygame.time.Clock()
running = True


# TODO: crie o labirinto, da forma como quiserem
# Lembrem-se de adicionar a um grupo

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

    # TODO conferir colisão usando pygame.sprite.spritecollide(grupo1, grupo2, True)




    # TODO você pode usar sons da seguinte forma:
    # sound = pygame.mixer.Sound("sound.wav")
    # pygame.mixer.Sound.play(sound)
    # Você pode baixar sons de efeitos sonoros gratuitos em https://mixkit.co/free-sound-effects/
    # ou https://www.findsounds.com/category.html

    # group_walls.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
