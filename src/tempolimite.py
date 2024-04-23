#limite de tempo
import pygame

class Cronometro(pygame.ACTIVEEVENT):
    def __init__(self, coeficiente_dificuldade, tempo_especial = 1):
        tempo_limite = (180.0 * tempo_especial) / coeficiente_dificuldade