"""
Desafio proposto:

Criar um programa que irá calcular o percentual de gastos de um salário de
um usuário.

Desafio proposto inicialmente recebendo valores pré-definidos nas variáveis.

"""

salario = float(input(f"Informe o seu salário\n"))
gasto = float(input(f"Informe o seu gasto\n"))

porcentagem = gasto / salario
# round(x,y) função responsável por arredondar o a quantidade de casas decimais
# print(f"O seu gasto corresponde a {round(porcentagem *100,2)}%")
# Segunda forma que pode-se limitar
print(f"O seu gasto corresponde a {'{:.2f}'.format(porcentagem * 100)}")
