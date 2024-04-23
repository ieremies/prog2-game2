import timeit
import time

espera = float(input("Quanto tempo deseja esperar? "))
inicio = timeit.default_timer()
i = 0
uau = 0
while timeit.default_timer() - inicio < espera:
    if i == 1:
        uau = timeit.default_timer() - inicio
    if i > 1:
        time.sleep(0.01)
        agora = timeit.default_timer() - inicio
        print("Passou ", agora, "segundos")
    i += 1
print(i)
print(uau)