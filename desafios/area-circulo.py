import math
import os
import sys
import errno


def circulo(raio):
    pi = math.pi
    return pi * raio ** 2


def alerta():
    print(f"É necessário informar o raio do circulo.\n"
          f"syntax: {sys.argv[0][-15:]} <raio>")
    os.system('pause')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        alerta()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        alerta()
        print('O raio deve ser um valor numérico.')
        os.system('pause')

    else:
        entrada = sys.argv[1]
        entrada = float(entrada)
        area = circulo(entrada)
        area = format(area, '.2f')
        print(f'A area do circulo é {area}cm²')
        print('Aperte qualquer tecla para sair.')
        os.system('pause > nul')
