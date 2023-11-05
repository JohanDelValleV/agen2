import matplotlib.pyplot as plt
from individuo_mejorado import Individual
from population import generate_childrens, generate_population
from utils import fitness, population_average
from cons import INITIAL_POPULATION_VALUE, POPULATION_SIZE, SELECTION, ITERATION_TIMES
import matplotlib
matplotlib.use('TkAgg')


average_population: list[float] = []
best_population: list[float] = []
worst_population: list[float] = []
population: list[Individual] = generate_population(size=POPULATION_SIZE)
first_generation: bool = True

for _ in range(ITERATION_TIMES):
    childrens: list[Individual] = generate_childrens(
        population, first_generation)

    population = population + childrens
    local_population = []

    for individual in population:
        values = []
        index = 0

        for _ in range(0, 11):
            values.append(int(individual.value[index:(index+20)], 2))
            index += 20

        if sum(values) <= INITIAL_POPULATION_VALUE and 0 not in values:
            individual.fitness = fitness(values)
            local_population.append(individual)

    sorted_population = sorted(
        local_population, key=lambda x: x.fitness, reverse=True)

    best_population.append(sorted_population[0].fitness)
    average_population.append(population_average(sorted_population))
    worst_population.append(
        sorted_population[len(sorted_population)-1].fitness)

    poblacion = sorted_population[0:SELECTION]
    first_generation = False


total_investment: int = 0
index: int = 0
for i in range(1, 12):
    y = int(poblacion[0].value[index:(index+20)], 2)
    print(f'Y{i} = {y}')
    total_investment += y
    index += 20
print(f'Total investment = {total_investment}')


def draw_graphic():
    plt.title("Fitness evolution")
    plt.plot(best_population, color="green", label="Best population")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.plot(average_population, color="blue", label="Average population")
    plt.plot(worst_population, color="red", label="Worst population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    draw_graphic()
