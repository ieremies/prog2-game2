import timeit
import time
import tempolimite


class Dificuldade:
    def __init__(self):
        super().__init__()

    def aumentar_dificuldade(self, tempo_limite, taxa_aumento):
        dificuldade = 1  # Definir a dificuldade inicial
        tempo_original = timeit.default_timer()
        tempo_decorrido = 0

        # Simular a execução de alguma atividade
        print("Realizando atividade com dificuldade", dificuldade)

        tempo_decorrido = timeit.default_timer() - tempo_original

        # Verificar se é hora de aumentar a dificuldade
        if tempo_decorrido >= tempo_limite:
            dificuldade += taxa_aumento
            print("Dificuldade aumentada para", dificuldade)
            tempo_decorrido = 0  # Resetar o tempo decorrido

        # Aqui você pode adicionar outras condições para controlar a execução ou encerrar o loop


# Exemplo de uso
# aumentar_dificuldade(tempo_limite=5, taxa_aumento=1)
