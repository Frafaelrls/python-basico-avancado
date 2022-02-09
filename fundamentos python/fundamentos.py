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

a = 10.5  # tipo flout
b = 5  # tipo int
c = 'Texto'  # tipo string
print(a + b)

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
