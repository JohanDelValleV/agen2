# Utils.py
from random import random, randint
from typing import Final
from collections import deque
from individuo_mejorado import Individual

mutate_probability_per_bit: Final[float] = 0.05

Z: Final[list[float]] = [-0.00015576, -0.00011687, 0.00052016, 0.00084352, 0.00064934, -
                         0.00015576, 0.00029955, 0.00117849, -0.00096882, 0.00011396, -
                         0.00103149]


def mutate(individual: str) -> str:
    """Mutates an individual by its mutate probability

    Args:
        individual (list[str]): bits array

    Returns:
        str: a mutated individual
    """
    individual_list: list[str] = list(individual)
    for index, bit in enumerate(individual):
        random_mutate: float = random()
        if random_mutate <= mutate_probability_per_bit:
            individual_list[index] = '0' if bit == '1' else '1'

    return ''.join(individual_list)


def fitness(values: list) -> int:
    """Calculates fitness

    Args:
        values (list): a values list

    Returns:
        int: sum of Z[i]*values[i]
    """
    _sum: int = 0
    for i in range(len(Z)):
        _sum += Z[i]*values[i]

    return _sum


def int_to_binary(dec: int) -> str:
    decode = deque([])
    if dec == 0:
        decode.insert(0, '0')
    else:
        while dec != 0:
            decode.insert(0, '1')if dec % 2 != 0 else decode.insert(0, '0')
            dec = int(dec/2)
    while len(decode) != 20:
        decode.insert(0, '0')

    return ''.join(decode)


def population_average(population: list[Individual]):
    return sum(individual.fitness for individual in population)/len(population)

def generate_random_number(a: int, b: int) -> int:
    return randint(a, b)
