"""
Sentença de código
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
Variáveis
- Em python não é necessário definir o tipo da variável o interpretador fará 
essa função.
- Atribuição de variáveis deve-se ter o identificador, o simbolo de atribuição
e o valor.
"""

casa = 10.5  # tipo flout
mesa = 5  # tipo int
cadeira = 'Texto'  # tipo string
print(casa + mesa )

"""
Comentários
- Devem ser usado acima da linha do código que será comentado
- Um programa que possui muitos comentários pode ser considerado um 
programa criado sem o uso de boas praticas
- O simples é melhor que o complexo; o complexo é melhor que complicado, 
deve-se criar programas usando bons nomes de variáveis, funções, classes o 
que vai facilita a leitura e interpretação do programa diminuindo o uso de 
comentários. 
"""

"""
Operadores aritméticos

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
Operadores relacionais
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
Operadores de atribuição
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

