import sys

# Gerador de números que consome uma quantidade menor de memória.
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) # Saída 0
print(next(generator)) # Saída 4
print(next(generator)) # Saída 16
print(next(generator)) # Saída 36
print(next(generator)) # Saída 64
#print(next(generator)) # Erro!

# Teste de memoria

lista = [i ** 2 for i in range(1000) if i % 2 == 0]
generator = (i ** 2 for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))