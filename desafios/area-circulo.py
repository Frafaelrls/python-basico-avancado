import math
import os

pi = math.pi

raio = input('Insira o raio do circulo em cm\n')
raio = float(raio)

area = pi * raio**2
area = format(area, '.2f')
print(f'A area do circulo é {area}cm²')
print('Aperte qualquer tecla para sair.')
os.system('pause > nul')
