import random
import individual
VALOR_INICIAL = 1000000

poblacion = []
decremento = 10
for _ in range(20):
    value = random.randint(1, VALOR_INICIAL-decremento)
    value = f'{value:20b}'.format(6)
    # print(value)
    decremento -= 1
    poblacion.append(individual.Individuo(value, individual.fitness(value), 0))

poblacion = sorted(poblacion, key=lambda x: x.fitness)
print(poblacion)
