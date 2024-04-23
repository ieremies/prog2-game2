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
import telainicial
import chao
import estrelitos
import textos
import inspetora
import banheiro
import timeit
import missoes

# Inicializa o jogo
pygame.init()

# Configura o display
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))

# a tela inicial
tela = telainicial.TelaInicial(width, height)
group_tela = pygame.sprite.Group()
group_tela.add(tela)

# o chao
floor = chao.Chao(width, height)
group_chao = pygame.sprite.Group()
group_chao.add(floor)

##o banheiro##
bath = banheiro.Banheiro(width, height)
group_banheiro = pygame.sprite.Group()
group_banheiro.add(bath)

## estrelitos ##
# criar um grupo de sprites para os estrelitos
group_estrelito = pygame.sprite.Group()
# adicionar os estrelitos ao grupo
n_estrelitos = 20

for _ in range(n_estrelitos):
    group_estrelito.add(estrelitos.Estrelitos(width, height))

# as missoes
# criar mais de um grupo (sao desenhadas em momentos diferentes))
group_missoes_lavarmao = pygame.sprite.Group()
group_missoes_descarga = pygame.sprite.Group()
group_missoes_lavarmao2 = pygame.sprite.Group()

# criar missoes e adicionar missoes (setas) aos grupos
missao_lavarmao = missoes.Missoes(40, width // 5, height * 3 // 4, 135.0)
group_missoes_lavarmao.add(missao_lavarmao)

missao_descarga = missoes.Missoes(40, 0.45 * width, 0.8 * height, 135.0)
group_missoes_lavarmao.add(missao_descarga)

missao_lavarmao2 = missoes.Missoes(40, width // 5, height * 3 // 4, 135.0)
group_missoes_lavarmao2.add(missao_lavarmao2)


# o jogador
p = player.Player(width, height)
# criar um grupo de sprites para o jogador
group_player = pygame.sprite.Group()
group_player.add(p)

# inspetora
insp = inspetora.Inspetora(100, 100)
group_IA = pygame.sprite.Group()
group_IA.add(insp)

# paredes
group_wall = pygame.sprite.Group()
largura_parede = 5
# Parede de cima
group_wall.add(wall.Wall(0, 0, width - largura_parede, largura_parede))
# Parede de baixo
group_wall.add(wall.Wall(0, height - largura_parede, width, largura_parede))
# Parede da esquerda
group_wall.add(wall.Wall(0, 0, largura_parede, height - largura_parede))
# Parede da direita
group_wall.add(
    wall.Wall(width - largura_parede, 0, largura_parede, height - largura_parede)
)

n_puffs = 30
for _ in range(n_puffs):
    group_wall.add(
        puff.Puff(width, height, 15)
    )  # obs: 15 esta em player, pygame.surface

# Define a cor branco
white = (255, 255, 255)
blue = (0, 0, 255)

# Cria um relógio
clock = pygame.time.Clock()
taxa_frame = 60
running = True
carregar_jogo = False
player_vivo = True
inicio = timeit.default_timer()
numero_frames = 0
cor = 0
legenda_inicial = [
    "Aperte a tecla espaço para jogar",
    (100, height - 50),
    (cor, cor, cor),
    screen,
    "Arial",
    40,
]
coracao_legenda = 0
controle = 0
inicio_jogo = False
perseguir = False

while running:
    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if carregar_jogo == False:
        screen.fill(blue)
        if coracao_legenda == 0:
            legenda_inicial = [
                "Aperte a tecla espaço para jogar",
                (100, height - 50),
                (cor, 0, 0),
                screen,
                "Arial",
                40,
            ]
            if cor <= 254 and controle == 0:
                cor += 1
            elif cor == 255 or (controle == 1 and cor != 0):
                cor -= 1
                controle = 1
            elif cor == 0:
                controle = 0
                coracao_legenda = 1
        textos.escrever(
            legenda_inicial[0],
            legenda_inicial[1],
            legenda_inicial[2],
            legenda_inicial[3],
            legenda_inicial[4],
            legenda_inicial[5],
        )

        if coracao_legenda == 1:
            legenda_inicial = [
                "Aperte a tecla espaço para jogar",
                (100, height - 50),
                (0, cor, 0),
                screen,
                "Arial",
                40,
            ]
            if cor <= 254 and controle == 0:
                cor += 1
            elif cor == 255 or (controle == 1 and cor != 0):
                cor -= 1
                controle = 1
            elif cor == 0:
                controle = 0
                coracao_legenda = 2
        textos.escrever(
            legenda_inicial[0],
            legenda_inicial[1],
            legenda_inicial[2],
            legenda_inicial[3],
            legenda_inicial[4],
            legenda_inicial[5],
        )

        if coracao_legenda == 2:
            legenda_inicial = [
                "Aperte a tecla espaço para jogar",
                (100, height - 50),
                (0, 0, cor),
                screen,
                "Arial",
                40,
            ]
            if cor <= 254 and controle == 0:
                cor += 1
            elif cor == 255 or (controle == 1 and cor != 0):
                cor -= 1
                controle = 1
            elif cor == 0:
                controle = 0
                coracao_legenda = 0
        textos.escrever(
            legenda_inicial[0],
            legenda_inicial[1],
            legenda_inicial[2],
            legenda_inicial[3],
            legenda_inicial[4],
            legenda_inicial[5],
        )

        if keys[pygame.K_SPACE]:
            carregar_jogo = True
            inicio_jogo = True
        group_tela.draw(screen)

    if carregar_jogo == True:
        # if inicio_jogo == True:
        #     screen.fill(white)
        #     group_banheiro.draw(screen)
        #     group_missoes_lavarmao.draw(screen)
        #     posicao_mouse = pygame.mouse.get_pos()
        #     # if event.type == pygame.MOUSEBUTTONDOWN:
        #     #     if group_missoes_lavarmao.collidepoint(posicao_mouse) and event.button == 1:
        #     #         pygame.sprite.groupcollide(group_missoes_lavarmao, posicao_mouse, True, False)

        if inicio_jogo == True or perseguir == True:
            group_chao.draw(screen)  # pinta a tela de branco
            group_estrelito.draw(screen)
            # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
            if player_vivo:
                keys = pygame.key.get_pressed()
                colidiu = pygame.sprite.groupcollide(
                    group_player, group_wall, False, False
                )
                coletou = pygame.sprite.groupcollide(
                    group_player, group_estrelito, False, True
                )
                if coletou:
                    p.coletar_estrelito()
                p.move(keys, colidiu)
                group_player.draw(screen)
            group_wall.draw(screen)

            # inspetora
            # detectar a colisão entre o player e a inspetora e quando ela for True o player é deletado/morre
            colidiu_pi = pygame.sprite.groupcollide(group_player, group_IA, True, False)
            if colidiu_pi:
                player_vivo = False
            # calcular as diferenças de localização e ativação da função
            diferenca_x = p.rect.x - insp.rect.x
            diferenca_y = p.rect.y - insp.rect.y
            insp.perseguir(diferenca_x, diferenca_y, 1)
            group_IA.draw(screen)

            while pygame.sprite.groupcollide(group_estrelito, group_wall, False, True):
                print("um estrelito colidiu com um puff")
                group_wall.add(puff.Puff(width, height, 15))
                group_wall.draw(screen)

    pygame.display.update()
    numero_frames += 1
    clock.tick(taxa_frame)

pygame.quit()
sys.exit()
