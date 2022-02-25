import math
import os
import sys


def circulo(raio):
    pi = math.pi
    return pi * raio ** 2


if __name__ == '__main__':
    entrada = sys.argv[1]
    entrada = float(entrada)
    area = circulo(entrada)
    area = format(area, '.2f')
    print(f'A area do circulo é {area}cm²')
    print('Aperte qualquer tecla para sair.')
    os.system('pause > nul')
