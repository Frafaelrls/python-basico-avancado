import math
import os


def circulo(raio):
    pi = math.pi
    area = pi * raio ** 2
    area = format(area, '.2f')
    print(f'A area do circulo é {area}cm²')
    print('Aperte qualquer tecla para sair.')
    os.system('pause > nul')


if __name__ == '__main__':
    entrada = input('Insira o raio do circulo em cm\n')
    entrada = float(entrada)
    circulo(entrada)
