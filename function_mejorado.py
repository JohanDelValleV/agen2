import matplotlib.pyplot as plt
import individuo_mejorado as individual
import random
import math
import matplotlib
matplotlib.use('TkAgg')


probabilidad_mutar_por_individuo = 0.0005
numero_iteraciones = 100
POBLACION_SIZE = 200
poblacion = []
promedios = []
mejores = []
peores = []
VALOR_INICIAL = 1000000
SELECCION = 1000


def conv_binario(dec):
    decode = []
    final = ''
    if dec == 0:
        decode.insert(0, '0')
    else:
        while dec != 0:
            if int(dec) % 2 != 0:
                decode.insert(0, '1')
            else:
                decode.insert(0, '0')
            dec = int(dec/2)
    while len(decode) != 20:
        decode.insert(0, '0')
    for n in decode:
        final += n
    return final


def promedio(poblacion):
    return sum(individuo.fitness for individuo in poblacion)/len(poblacion)


for _ in range(POBLACION_SIZE):
    individuo_temp = ''
    decremento = 10
    for _ in range(0, 11):
        numero = random.randint(1, VALOR_INICIAL-decremento)
        value = conv_binario(numero)
        decremento -= 1
        VALOR_INICIAL = VALOR_INICIAL - numero
        individuo_temp += value
    poblacion.append(individual.Individuo(individuo_temp, 0))
    VALOR_INICIAL = 1000000
generacion0 = True
for _ in range(numero_iteraciones):
    children = []
    for _ in range(1000):
        parent_1 = poblacion[0]
        if generacion0:
            parent_1 = poblacion[random.randint(0, len(poblacion)-1)]

        parent_2 = poblacion[random.randint(0, len(poblacion)-1)]
        value1 = parent_1.value[0:110] + parent_2.value[110:220]
        value2 = parent_2.value[0:110] + parent_1.value[110:220]
        value1 = individual.mutar(value1)
        value2 = individual.mutar(value2)

        children.append(individual.Individuo(value1, 0))
        children.append(individual.Individuo(value2, 0))

    poblacion = poblacion+children
    mejor_poblacion = []

    for individuo in poblacion:
        variables = []
        posicion = 0

        for i in range(0, 11):
            variables.append(int(individuo.value[posicion:(posicion+20)], 2))
            posicion += 20

        suma = sum(variables)
        if suma <= 1000000:
            if not (0 in variables):
                individuo.fitness = individual.fitness(variables)
                mejor_poblacion.append(individuo)

    sorted_ind = sorted(mejor_poblacion, key=lambda x: x.fitness, reverse=True)

    mejores.append(sorted_ind[0].fitness)
    promedios.append(promedio(sorted_ind))
    peores.append(sorted_ind[len(sorted_ind)-1].fitness)

    poblacion = sorted_ind[0:SELECCION]
    generacion0 = False


print(poblacion[0])
Z = [-0.00015576, -0.00011687, 0.00052016, 0.00084352, 0.00064934, -
     0.00015576, 0.00029955, 0.00117849, -0.00096882, 0.00011396, -
     0.00103149]
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
