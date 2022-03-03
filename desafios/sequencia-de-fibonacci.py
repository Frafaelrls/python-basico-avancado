#!/usr/local/bin/python3

"""
Sequência de Fibonacci consiste numa sucessão infinita de números que obedecem
um padrão em que cada elemento subsequente é a soma dos dois anteriores.
Assim, após 0 e 1, vêm 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc
"""


def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while limite > ultimo:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(10)


def fibonacci_packing(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while limite > ultimo:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonacci_packing(10)


def fibonacci_list(limite):
    resultado = [0, 1]
    # Enquanto o último item da lista for menor que o limite
    while resultado[-1] < limite:
        # Soma os dois últimos itens da lista e adiciona na lista
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci_list(100):
        print(fib)


def fibonacci_sum(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        # Soma os dois itens da lista e adiciona o resultado à lista
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci_sum(100):
        print(fib)


def fibonacci_quantidade(quatidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        # Se o comprimento da lista for igual ao informado, pare
        if len(resultado) == quatidade:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci_quantidade(10):
        print(fib)
