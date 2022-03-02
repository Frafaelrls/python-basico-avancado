"""
Operadores lógicos

Descrição
Criar um programa de validação de atividades realizadas e com base nessa
validação gerar novas atividades, deve-se verificar se o trabalho foi
realizado ou não nos dias da semana 'terça' e 'quinta'; se às duas
atividades forem realizadas será comprado uma TV de 50' mais um sorvete; se
a penas uma atividade for realizada, será comprado uma TV de 32' mais um
sorvete; se nenhuma das atividades foram realizadas não será comprado nenhum
dos objetos.

Mapa verdade

Terça  | Quinta |    Shopping
 True  | True   | TV 50' + Sorvete
 True  | False  | TV 32' + Sorvete
 False | True   | TV 32' + Sorvete
 False | False  | Sem compras

"""

print("Informe com 1 se o trabalho foi concluído ou 0 se não foi.")
trabalho_terca = bool(input("O trabalho da terça-feira foi concluído?\n"))
trabalho_quinta = bool(input("O trabalho da quinta-feira foi concluído?\n"))

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print(f"Tv 50'= {tv_50} Tv 32'= {tv_32} Sorvete= {sorvete}"
      f" Saudável= {mais_saudavel}")

"""
Deve-se atentar durante o uso de operadores lógicos com as entrada 
fornecidas pelos usuários, as entradas serão no formato string e os 
operadores são no formato boolean, deve-se fazer a conversão para que a 
lógica funcione de maneira correta.
"""
