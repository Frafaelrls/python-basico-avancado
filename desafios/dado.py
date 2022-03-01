from random import randint


def sortear_dados():
    return randint(1, 6)


for i in range(1, 7):
    # Testando se o número é impar
    if i % 2 == 1:
        continue

    if sortear_dados() == i:
        print(f'Acertou o valor: {i}')
        break
else:
    print('Não acertou o valor')
