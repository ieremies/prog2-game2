try:
    import pygame
except ImportError:
    print("Pygame não está instalado. Instale-o com 'pip3 install pygame'")
    print("Confira o README.md para mais informações.")
    exit()

import asyncio
import player
import labirinto


async def main():
    # Inicializa o jogo
    pygame.init()

    # Configura o display
    width = 800
    height = 400
    screen = pygame.display.set_mode((width, height))

    # o jogador
    p = player.Player(width, height)
    # criar um grupo de sprites para o jogador
    group_player = pygame.sprite.Group()
    group_player.add(p)

    # Defini a cor branco
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

        # Muda a posição baseado na tecla pressionado
        # acho que aqui bota a logica da colisao
        # colisao = colisao(p1, p2)
        p.move(keys)

        # Desenha o jogador
        group_player.draw(screen)

        # desenha o labirinto
        # um monte de retangulo
        for x in range(0, 10):
            for y in range(0, 10):
                pygame.draw.rect(
                    screen, (0, 60, 128), (100 + x * 20, 100 + y * 20, 10, 10)
                )


        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())
