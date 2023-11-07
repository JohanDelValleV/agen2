# population.py

from cons import CHILDREN_POPULATION_SIZE, INITIAL_POPULATION_VALUE, INDIVIDUAL_SIZE
from individuo_mejorado import Individual
from utils import generate_random_number, int_to_binary, mutate


def generate_population(size: int, initial_value: int = INITIAL_POPULATION_VALUE) -> list[Individual]:
    population: list[Individual] = []
    for _ in range(size):
        individuo_temp = ''
        decremento = 10
        for _ in range(0, 11):
            numero = generate_random_number(1, initial_value-decremento)
            value = int_to_binary(numero)
            decremento -= 1
            initial_value = initial_value - numero
            individuo_temp += value
        population.append(Individual(individuo_temp, 0))
        initial_value = INITIAL_POPULATION_VALUE
    return population


def generate_childrens(population: list[Individual], first_generation: bool) -> list[Individual]:
    childrens: list[Individual] = []

    for _ in range(CHILDREN_POPULATION_SIZE):
        parent_1 = population[0] if first_generation else population[generate_random_number(
            0, len(population)-1)]

        parent_2 = population[generate_random_number(0, len(population)-1)]
        value1 = parent_1.value[0:110] + parent_2.value[110:INDIVIDUAL_SIZE]
        value2 = parent_2.value[0:110] + parent_1.value[110:INDIVIDUAL_SIZE]
        value1 = mutate(value1)
        value2 = mutate(value2)

        childrens.append(Individual(value1, 0))
        childrens.append(Individual(value2, 0))
    return childrens
