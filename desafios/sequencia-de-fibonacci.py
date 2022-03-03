#!/usr/local/bin/python3

"""
Sequência de Fibonacci consiste numa sucessão infinita de números que obedecem
um padrão em que cada elemento subsequente é a soma dos dois anteriores.
Assim, após 0 e 1, vêm 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc
"""


def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
