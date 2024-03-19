try:
    import pygame
except ImportError:
    print("Pygame não está instalado. Instale-o com 'pip3 install pygame'")
    print("Confira o README.md para mais informações.")
    exit()

import asyncio


async def main():
    # Inicializa o jogo
    pygame.init()

    # Configura o display
    width = 800
    height = 800
    screen = pygame.display.set_mode((width, height))

    # Configurações do jogador
    player_size = 50
    player_x = width // 2 - player_size // 2
    player_y = height // 2 - player_size // 2
    player_speed = 5

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
        if keys[pygame.K_w] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_s] and player_y < height - player_size:
            player_y += player_speed
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_d] and player_x < width - player_size:
            player_x += player_speed

        # Desenha o jogador
        pygame.draw.rect(
            screen, (0, 128, 255), (player_x, player_y, player_size, player_size)
        )

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())
