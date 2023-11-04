import matplotlib.pyplot as plt
from individuo_mejorado import Individual
from population import generate_childrens, generate_population
from utils import fitness, population_average
from cons import POPULATION_SIZE, SELECTION, ITERATION_TIMES
import matplotlib
matplotlib.use('TkAgg')


probabilidad_mutar_por_individuo = 0.0005
promedios = []
mejores = []
peores = []

population: list[Individual] = generate_population(size=POPULATION_SIZE)

first_generation: bool = True

for _ in range(ITERATION_TIMES):
    childrens: list[Individual] = generate_childrens(
        population, first_generation)

    population = population + childrens
    mejor_poblacion = []

    for individuo in population:
        variables = []
        posicion = 0

        for i in range(0, 11):
            variables.append(int(individuo.value[posicion:(posicion+20)], 2))
            posicion += 20

        suma = sum(variables)
        if suma <= 1000000 and 0 not in variables:
            individuo.fitness = fitness(variables)
            mejor_poblacion.append(individuo)

    sorted_ind = sorted(mejor_poblacion, key=lambda x: x.fitness, reverse=True)

    mejores.append(sorted_ind[0].fitness)
    promedios.append(population_average(sorted_ind))
    peores.append(sorted_ind[len(sorted_ind)-1].fitness)

    poblacion = sorted_ind[0:SELECTION]
    first_generation = False


print(poblacion[0])
total_inversion = 0
posicion = 0
for i in range(1, 12):
    y = int(poblacion[0].value[posicion:(posicion+20)], 2)
    print(f'Y{i} = {y}')
    total_inversion += y
    posicion += 20
print(f'Total inversion = {total_inversion}')


def dibujar():
    plt.title("Evolución del fitness")
    plt.plot(mejores, color="green", label="Mejor caso")
    plt.xlabel("Generaciones")
    plt.ylabel("Fitness")
    plt.plot(promedios, color="blue", label="Caso promedio")
    plt.plot(peores, color="red", label="Peor caso")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    dibujar()
