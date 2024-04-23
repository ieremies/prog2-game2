#textos do jogo
import pygame


#inicializar a parte do pygame que cuida das fontes
pygame.font.init()


# mostrar
def escrever(texto, posicao, cor, screen, fonte, tamanho): #screen e o tamanho do texto, a superficie
    # pegar a fonte
    #posicao[0] = pygame.get_
    font = pygame.font.SysFont(str(fonte), tamanho)
    objeto_texto = font.render(texto, True, cor)
    screen.blit(objeto_texto, posicao)