import random
import math

probabilidad_mutar_por_bit = 0.0005

Z = [-0.00015576, -0.00011687, 0.00052016, 0.00084352, 0.00064934, -
     0.00015576, 0.00029955, 0.00117849, -0.00096882, 0.00011396, -
     0.00103149]


class Individuo:
    def __init__(self, value, fitness, probability):
        self.value = value
        self.fitness = fitness
        self.probability = probability

    def __repr__(self):
        return '{'+str(self.value)+','+str(self.fitness)+','+str(self.probability)+'}'


def mutar(individuo):
    array_individuo = list(individuo)
    index = 0
    for bit in array_individuo:
        azar_mutar = random.random()
        if azar_mutar <= probabilidad_mutar_por_bit:
            if bit == '1':
                array_individuo[index] = '0'
            else:
                array_individuo[index] = '1'
        index += 1
    return ''.join(array_individuo)

# Partir individuo en 11


def fitness(value):
    # print(f'VALUE {value}')
    sumatoria = 0
    for i in range(len(Z)):
        sumatoria += (Z[i]*value[i])
    # print(f'SUMATORIA: {sumatoria}')
    return sumatoria
