import matplotlib.pyplot as plt
import individual
import random
import math
import matplotlib
matplotlib.use('TkAgg')


probabilidad_mutar_por_individuo = 0.0005
numero_iteraciones = 100
POBLACION_SIZE = 100
poblacion = []
promedios = []
mejores = []
peores = []
VALOR_INICIAL = 1000000


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


individuo_temp = ''
decremento = 10
for _ in range(POBLACION_SIZE):
    individuo_temp = ''
    decremento = 10
    for _ in range(0, 11):
        numero = random.randint(1, VALOR_INICIAL-decremento)
        value = conv_binario(numero)
        decremento -= 1
        VALOR_INICIAL = VALOR_INICIAL - numero
        print(VALOR_INICIAL)
        individuo_temp += value
    poblacion.append(individual.Individuo(
        individuo_temp, 0, 0))
    VALOR_INICIAL = 1000000

for _ in range(numero_iteraciones):
    children = []
    for padre in poblacion:
        parent_1 = poblacion[0]
        parent_2 = poblacion[-1]
        value1 = parent_1.value[0:110] + parent_2.value[110:220]
        value2 = parent_2.value[0:110] + parent_1.value[110:220]
        azar = random.random()
        # if azar <= probabilidad_mutar_por_individuo:
        value1 = individual.mutar(value1)
        # azar = random.random()
        # if azar <= probabilidad_mutar_por_individuo:
        value2 = individual.mutar(value2)

        children.append(individual.Individuo(value1, 0, 0))
        children.append(individual.Individuo(value2, 0, 0))

    poblacion = poblacion+children
    mejor_poblacion = []

    for individuo in poblacion:
        variables = []
        posicion = 0

        for i in range(0, 11):
            variables.append(int(individuo.value[posicion:(posicion+20)], 2))
            posicion += 20
            # if variables[i] >= 0 and variables[i] <= VALOR_INICIAL:
            #     individuo.fitness = individual.fitness(individuo.value)
            #     mejor_poblacion.append(individuo)

        suma = sum(variables)
        if suma <= 1000000:
            if not (0 in variables):
                individuo.fitness = individual.fitness(variables)
                mejor_poblacion.append(individuo)

    sorted_ind = sorted(mejor_poblacion, key=lambda x: x.fitness, reverse=True)

    mejores.append(sorted_ind[0].fitness)
    promedios.append(promedio(sorted_ind))
    peores.append(sorted_ind[len(sorted_ind)-1].fitness)

    poblacion = sorted_ind[0:100]


print(poblacion[0])
Z = [-0.00015576, -0.00011687, 0.00052016, 0.00084352, 0.00064934, -
     0.00015576, 0.00029955, 0.00117849, -0.00096882, 0.00011396, -
     0.00103149]
variables = []
posicion = 0
for i in range(0, 11):
    variables.append(int(poblacion[0].value[posicion:(posicion+20)], 2))
    posicion += 20
print(sum(variables))
for i in range(len(Z)):
    print(f'Y{i} = {variables[i]}')
articulo=[512,528,5128,303104,278530,258,2048,401408,2048,4230,768 ]
sumatoria = 0

for i in range(len(Z)):
    sumatoria += (Z[i]*articulo[i])
# print(f'SUMATORIA: {sumatoria}')
print(sumatoria)
def dibujar():
    # grafica = plt.plot()
    # grafica[0].set_title('Comparación entre datos reales y encontrados')
    # grafica[0].plot(x, y, color="red", label="Y reales")
    # grafica[0].plot(x, ya, color="black", label="Y encontrados")
    # grafica[0].legend(bbox_to_anchor=(1, 1), loc='center', borderaxespad=0.)
    # grafica[0].grid()
    #grafica.set_title('Evolución de fitness')
    plt.plot(mejores, color="green", label="Mejor caso")
    plt.plot(promedios, color="blue", label="Caso promedio")
    plt.plot(peores, color="red", label="Peor caso")
    #plt.legend(bbox_to_anchor=(1, 1), loc='center', borderaxespad=0.)
    plt.grid()
    #plt.set(xlabel='Generacion', ylabel='Fitness')
    # data = [x, y, ya]

    # table = plt.table(cellText=data, loc='bottom', rowLabels=[
    #                   'X', 'Yr', 'Ya'], bbox=[-0.14, -0.55, 1.25, .28])
    # table.auto_set_font_size(False)
    #plt.subplots_adjust(bottom=0.25)
    plt.show()


if __name__ == "__main__":
    # dibujar(individual.valores_x, individual.valores_y, valores_y_poblacion[0])
   dibujar()
