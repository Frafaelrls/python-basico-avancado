"""
*** Sentença de código ***

- Deve-se respeitar a indentação como as quebras de linhas dos comandos e
padrões de programação predefinidas.
- Deve-se ficar atento ao espaçamento durante o uso de comandos.
- É comumente usado uma sentença por linha
- Recomenda-se respeitar o limite de 79 carácteres por linha conforme a pep 8
"""
print('Hello World')
print(True)  # Tipo boolean, colocar com letra maiúscula
print(2 + 3)  # Operação aritmética
print(3 * ' muito')  # O texto será repetido três vezes
print('Concatenar o' + 2 * ' texto')  # concatenação do texto usando '+'
# print(2 + 'muito')  # Em caso de ambiguidade o programa não será rodado

"""
*** Variáveis ***

- Em python não é necessário definir o tipo da variável o interpretador fará 
essa função.
- Atribuição de variáveis deve-se ter o identificador, o simbolo de atribuição
e o valor.
"""

casa = 10.5  # tipo flout
mesa = 5  # tipo int
cadeira = 'Texto'  # tipo string
print(casa + mesa)

"""
*** Comentários ***

- Devem ser usado acima da linha do código que será comentado
- Um programa que possui muitos comentários pode ser considerado um 
programa criado sem o uso de boas praticas
- O simples é melhor que o complexo; o complexo é melhor que complicado, 
deve-se criar programas usando bons nomes de variáveis, funções, classes o 
que vai facilita a leitura e interpretação do programa diminuindo o uso de 
comentários. 
"""

"""
*** Operadores aritméticos ***

- São considerados como operadores binários; estruturalmente são montados 
com um operando, um operador e um segundo operando (1 + 1).
- Também são chamados de infix 
 
"""
print(1 + 2)  # Soma
print(4 - 7)  # Subtração
print(2 * 5.3)  # Multiplicação
print(9.4 / 3)  # Divisão
print(9.4 // 3)  # Divisão com o resultado apenas com números inteiros
print(2 ** 8)  # Exponenciação
print(10 % 3)  # Modulo 'Restante da divisão'

"""
*** Operadores relacionais ***

- Faz a comparação entre dois operandos e as respostas obtidas sempre vão ser 
'True' ou 'False'
"""
print(4 > 3)  # Maior que
print(4 >= 3)  # Maior ou igual que
print(1 < 2)  # Menor que
print(3 <= 1)  # Menor ou igual que
print(3 != 2)  # Diferente de
print(3 == 3)  # Igual que
print(2 == '2')  # Igual que

""" 
*** Operadores de atribuição ***
"""
a = 3
a = a + 7
print(a)
a += 5  # Atribuição somativa a = a +5
print(a)
a -= 3  # Atribuição subtrativa a = a - 3
print(a)
a *= 2  # Atribuição multiplicativa a = a * 2
print(a)
a /= 4  # Atribuição divisiva a = a / 4
print(a)
a %= 4  # Atribuição modular a = |a / 4|
print(a)
a **= 8  # Atribuição de potenciação a = a^8
print(a)
a //= 256  # Divisão obtendo resultados inteiros
print(a)

"""
*** Operadores Lógicos ***
"""

print(True or False)  # True
print(7 != 3 and 2 > 3)  # False

# Tabela verdade do and
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Tabela verdade do or

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Tabela verdade do xor
# Por não possuir um operador para a função "ou exclusivo" foi usado "!=".
# O uso do '!=' não faz parte das boas praticas de programação.

print(True != True)  # False
print(True != False)  # True
print(False != True)  # True
print(False != False)  # False

# Operador de Negação (unário)

print(not True)  # False
print(not False)  # True
print(not 0)  # True
print(not 1)  # False

# Cuidado!
# Fica atendo quanto ao uso dos operadores não confundir com operadores bit
# a bit como os listados a baixo.

print(True & True)  # True and True = True
print(True | True)  # True or True = True
print(True ^ True)  # True xor True = False

# Em bit a bit a comparação é realizada em binário, transforma-se o numero
# para binário e é realizada a comparação.
# Deve-se ter atenção no momento do uso não utilizar o bit a bit quando for
# necessário usar os operadores lógicos ou o inverso.

# and bit a bit
# print(3 & 2)
# 3 = 11
# 2 = 10
# R = 10 R= resultado
# Conforme o exemplo acima,comparando cada bit retornando o 2 (10 em binário)

# or bit a bit
# print(3 | 2)
# 3 = 11
# 2 = 10
# R = 11 R= resultado
# Conforme o exemplo acima, o resultado é 3 (11 em binário)

# xor bit a bit
# print(3 ^ 2)
# 3 = 11
# 2 = 10
# R = 01 R= resultado
# Conforme o exemplo acima, o resultado é 1 (01 em binário)

# Um pouco de realidade
# Calculando se o usuário deixou mais de 20% de saldo

saldo = 1000
salario = 4000
despesas = 2970

# Usando operadores lógicos
saldo_positivo = saldo > 0
despesas_controladas = salario - despesas > 0.2 * salario
meta_logica = saldo_positivo and despesas_controladas
print(f"Resultado usando operadores lógicos = {meta_logica}")

# Usando operadores bit a bit
saldo_positivo = saldo > 0
despesas_controladas = salario - despesas > 0.2 * salario
meta_bit = saldo_positivo & despesas_controladas
print(f"Resultado usando operadores bit a bit = {meta_bit}")

"""
*** Operadores Unários ***

São operadores que trabalham com apenas um operando
"""

b = -3
print(-b)  # Transforma o valor da variável em positivo
print(not 0)
print(not 1)  # Valores acima de zero são true

"""
*** Operadores Ternário ***

É o momento em que temos três operandos para uma sentença

"""

esta_chovendo = True
# Na linha a seguir se a variável for verdadeira será considerado o operando
# mais próximo dela como resultado.
print("Hoje estou com roupas " + ("secas.", "molhadas.")[esta_chovendo])
print("Hoje estou com roupas " + ("molhadas." if esta_chovendo else "secas."))

"""
*** Operadores de Membros e Identidade ***
"""

# Operador de membro
lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)  # Dois está na lista? True - Dois está presente
print('Ana' not in lista)  # Ana não está na lista. False - Ana está presente

# Operador de Identidade

x = 3
y = x
z = 3

print(x is y)  # x é y? True
print(y is z)  # y é z? True
print(x is not z)  # x não é z. False

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)  # Lista A é a Lista B? True
print(lista_b is lista_c)  # Lista B é a Lista C? False

"""
No exemplo que utiliza as listas elas vão ser diferentes por ocuparem um 
espaço diferente de memória, cada lista vai está em um espaço, quando 
criamos a lista A é colocado 3 valores em um espaço de memória e quando 
falamos que a Lista B é igual a lista A, definimos que aquela variável 
possui os mesmo valores que se encontram naquele espaço de memória; Quando 
definimos a lista C é colocado 3 valores em um outro espaço de memória, 
mesmo que os valores armazenados sejam idênticos as listas são consideradas 
diferentes por estarem em espaços de memória diferente.
Se alterarmos colocando ou retirando os valores na lista A será modificado 
na lista A e B; Se alterarmos na lista C será alterado apenas na lista C.
"""

"""
*** Builtins ***

É um módulo interno do python que disponibiliza algumas funções para o uso 
no dia a dia da programação, como por exemplo as funções 'print', 'str', 
'type', 'vars'... e as demais; para poder ter acesso as outras funções 
disponíveis nesse módulo basta usar o comando a seguir.

print(dir(__builtins__))

Uma outra função que pode ser utilizada para aprendizado é a função help, 
a partir dela será possível buscar informações sobre os comandos utilizados 
na linguagem python.

Com esse comando será disponibilizado durante a execução do programa um a 
documentação das funções. Um exemplo de uso, pode-se buscar pela descrição 
de uso do comando 'print', seguindo os passos abaixo.

help(print)

Deixando sem um argumento entre parenteses, você poderá buscar por outros 
comandos que sejam do seu interesse, digitando diretamente no terminal os 
nomes dos comandos, para finalizar o programa após pequisas, basta colocar 
o comando 'quit'.
   
"""
