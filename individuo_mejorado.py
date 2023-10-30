# Individuo_mejorado.py
from dataclasses import dataclass


@dataclass
class Individual:
    value: int
    fitness: int

    def __repr__(self):
        return '{'+str(self.value)+','+str(self.fitness)+'}'
