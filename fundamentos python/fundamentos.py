"""
*** Sentença de código ***

- Deve-se respeitar a indentação como as quebras de linhas dos comandos e
padrões de programação predefinidas.
- Deve-se ficar atento ao espaçamento durante o uso de comandos.
- É comumente usado uma sentença por linha
- Recomenda-se respeitar o limite de 79 carácteres por linha conforme a pep 8
"""
import math

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

Deixando sem um argumento entre parênteses, você poderá buscar por outros 
comandos que sejam do seu interesse, digitando diretamente no terminal os 
nomes dos comandos, para finalizar o programa após pesquisas, basta colocar 
o comando 'quit'.
   
"""

"""
*** Conversão de tipos ***

Podemos fazer a conversão de tipos usando funções presentes no builtins; 
algumas das funções que podemos utilizar são:
    str() - Converte para string
    int() - Converte para integer
    flout() - Converte para floating

Para o uso colocamos o que queremos converter dentro dos parênteses.

x = '3'
print(int(x))
 
Devemos está atentos quanto aos valores a serem convertidos e as limitações; 
Uma conversão de string para int dever-se usar partes textos que podem 
ser transformados em um numero inteiro.

x = '4 texto'
print(int(x))

No exemplo acima será apresentado o seguinte erro 'ValueError', o python não 
será capaz de transformar o texto em um numero inteiro da base 10; por esse 
motivo devemos está atendo quanto ao texto que queremos converter. 

A linguagem Python não fará adivinhações no que queremos fazer, devemos ser 
explícitos quando a criação da lógica. No exemplo abaixo temos um má uso de 
mistura de tipos diferentes, que gerará o erro 'TypeError;

print(1 + '2')

Por estarmos tentando fazer uma operação entre uma variável do tipo int e 
uma do tipo str o python não irá tentar adivinhar o que queremos fazer, 
devemos ser explícitos nos nosso pedidos. Um método de correção desse erro é o
uso das conversões através das funções.

print(1 + int('2'))

Vemos acima um modo de deixarmos explicito o nosso desejo, com isso 
retiramos as possibilidades que estavam em aberto, sendo elas a soma das 
duas variáveis ou a concatenação das duas variáveis, como a linguagem Python 
não faz a escolhas, devemos deixar explicito para ele que queremos efetuar a 
soma e um dos modos que temos é fazer a conversão do tipo 'str' para 'int'.   
"""

print(1 + int('2'))

"""
*** Coerção Automática ***

Em alguns momentos o python fará a conversão das variáveis de forma 
automática; durante a divisão de números inteiros vamos ver essa conversão 
acontecendo.

x = 10 / 2
print(x)
print(type(x))

5.0
<class 'float'>

Na linguagem python mesmo que o resultado de uma divisão seja um número inteiro
ele será convertido para 'float'; 

Em uma conversão onde queremos como resultado apenas os números inteiros 
usando o comando '//' e utilizamos um numero do tipo float, o python irá 
apresentar o resultado como do tipo 'float' como visto a baixo; 

z = 10 // 3.3
print(z)
print(type(z))

3.0
<class 'float'>

Com o uso da limitação de resultados através do '//' faremos o uso apenas 
de números do tipo 'int';

t = 10 // 3
print(t)
print(type(t))

3
<class 'int'>

Nesse momento recebemos um resultado do tipo 'int', devido a exclusão de 
números decimais e o trabalho apenas com números inteiros, o python não faz 
a conversão do resultado para o tipo 'flout'.

Outro momento que ocorre a coerção automática é durante a soma de dois números
de tipos diferentes; prevalecendo o tipo 'float'.

y = 2 + 2.0
print(y)
print(type(y))

4.0
<class 'float'>

As variáveis do tipo 'float' são capazes de armazenar mais dados que as
variáveis do tipo 'int', podemos concluir que as variáveis do tipo 'float' 
possuem uma dominância sobre as do tipo 'int', fazendo com que em operações 
com os dois tipos podemos antecipar que o resultado será do tipo 'float' 
devido a dominância. 
 
"""
x = 10 / 2
print(x)
print(type(x))

y = 2 + 2.0
print(y)
print(type(y))

z = 10 // 3.3
print(z)
print(type(z))

t = 10 // 3
print(t)
print(type(t))

"""
*** Tipos numéricos ***

Podemos verificar através da função dir() quais são as funções de cada tipo.

- int()  
    Números do tipo int são os números inteiros, a sigla vem do inglês 
    'integer' que significa 'inteiro' em português.       
- float()
    Números do tipo float são os números decimais, a sigla vem do floating 
    point ou ponto flutuante em português.
    
    Em algumas operações do tipo 'float' vamos obter resultados que não são 
    esperados.
    
    print(1.1 + 2.2)
    
    3.3000000000000003
    
    Esse resultado é apresentado devido a forma padrão de modelo de 
    implementação interna de operações aritméticas usadas pelas linguagens 
    de programação. 
    
    Os números do tipo 'float' são representados no hardware dos computadores 
    como decimais binários.
    
    x = 0.125
    y = 1 / 10 + 2 / 100 + 5 / 100  
    z = 0.001
    w = 0 / 2 + 0 / 4 + 1 / 8
    
    x == y
    y == z
    z == w
    
    No exemplo acima temos a representação do mesmo número, nos dois 
    primeiros momentos (x e y) temos a representação na base 10 e nos dois 
    últimos momentos (z e w) temos a representação do número na base 2.
    
    Nessas representações vão ocorrer momentos que uma fração não pode ser 
    representada exatamente como uma fração de base 2, quando realizamos a 
    conversão encontraremos como resultado uma dizima periódica.
    
    X= 1/10 
    y= 0.1
    z= 0.0001100110011001100110011001100110011001100110011...
    
    Temos acima a representação da fração (x) sua representação em 'float 
    (y) e por fim sua representação em binário (z); a representação em 
    binário retorna uma dizima periódica; Quando realizamos operações com os 
    números do tipo float as maquinas atuais ira trabalhará com uma 
    aproximação de 53 bits contando do mais significativo na base 2.
    
    Devido essa aproximação teremos algumas operações que retornarão um 
    resultado diferente do esperado, devido ao nível de precisão utilizado.
    
    print(0.1 + 0.1 + 0.1 == 0.3)
    False
    
    A comparação entre as somas e o resultado acima, será 'False', devido a 
    precisão de valores e a dizima periódica na base 2.
    
    Em casos onde podemos trabalhar com uma precisão menor, podemos utilizar a
    função 'format()' para representar um número limitado de casas decimais.
    
    x = math.pi
    y = math.pi
    
    print(f'x= {x}')

    y = format(y, '.3f')
    print(f'y= {y}')
    
    x= 3.141592653589793
    y= 3.142
    
    Os valores apresentados com o uso do 'format' terão os decimais 
    limitados na sua apresentação visual e arredondando os valores 
    apresentados.
           
"""

""""
*** Tipo String ***

Podemos verificar através da função dir() quais são as funções de cada tipo.

Podemos acessar partes da variável do tipo 'string', utilizando o índice de 
posicionamento dos carácteres.


    x = 'Pedro Paulo'
    print(x[0])

    p

Podemos acessar também utilizando a contagem inversa de posições, para isso 
basta fornecer um número negativo;


x = 'Pedro Paulo'
    print(x[-2])

    l


Para acessarmos em um intervalo utilizamos o dois pontos (:) para definir 
como será recebido os resultados.


     x = 'Pedro Rafael'
     
     # Para acessar os elementos iniciando a partir da posição 6 e indo até 
     o final.
     
     print(x[6:])
     Rafael
     
     # Para acessar a partir do final, usando números negativos.
     
     print(x[-5:])
     Rafael
     
     # Saindo do início e parando em um índice. Nesse caso a posição 5 é 
     excludente, o valor salvo na posição 5 não será considerado.
     
     print(x[:5])
     Pedro
     
     print(x[:4])
     Pedr
     
     # Definindo o ponto de inicio e final do intervalo.
     
     print(x[6:12])
     Rafael
     
Podemos aprimorar essa busca por intervalo adicionando 'passos', que são 
comandos que definiram como os valores serão apresentados.

    x = '1234567890'
    
    # Buscando os valores intercalados de 2 em 2 em todo intervalo da string.
    
    print(x[::2])     
    13579
    
    # Limitando o inicio de busca do intervalo.
    
    print(x[1::2])
    24680 
    
    # Invertendo uma string, indo do final até o começo usando um passo 
    negativo; podendo trabalhar buscando valores intercalados.
    
    print(x[::-1])
    0987654321  
    
    
As strings são imutáveis, se fizermos a tentativa de alteração de um dos 
caracteres, será retornado um erro de tipo, avisando que objetos do tipo 
string não suportam atribuição


    x = 'Paulo Pedro'
    # Tentativa de atribuição
    x[0] = 'S'
    print(x[0])

    TypeError: 'str' object does not support item assignment


Para a manipulação de textos com múltiplas linhas, podemos usar alguns 
comandos presentes na função 'str';
    \n = Nova linha, o interpretador considerará que após esse comando o 
         texto deve ser apresentado em uma nova linha.   
    \t = Tabular, será feito a tabulação do texto após o comando.
    '\' = Quebra de linha,esse comando (contra barra, alt + 92 em teclados 
          americanos) será usado durante a programação, ele não afetara como a
          string será apresentada para o usuário, será usada para deixar o 
          programa com um visual melhor; Conforme a PEP 8 recomenda-se o limite
          de 79 caracteres por linha de código,para que isso seja possível, 
          usa-se a contra barra para mostrar que a string continua na próxima
          linha.
          
          Exemplo:
          x = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \ 
              "Phasellus a lacus orci."
           
          Deve-se fechar com aspas o local onde será feito a partição da string
          logo após adicionamos a contra barra e é dada a continuidade da 
          string abrindo e fechando as aspas.
    
Devemos está atentos quando ao uso dos caracteres especiais para não 
confundirmos com parte do texto.


    x = 'Nullam facilisis turpis ut placerat dictum; \nullam auctor finibus ' \
    'aliquet.'
    print(x)
    
    Nullam facilisis turpis ut placerat dictum; 
    ullam auctor finibus aliquet.


No exemplo a cima, a segunda recorrência da palavra 'nullam' perde o 'n' 
quando usamos o comando print, isso por que o Python compreendeu que ele seria 
parte do comando para quebra de linha e não uma parte do texto, devemos está 
atentos durante o uso do comando '\t'; para efetuar a correção, 
basta repetir a letra 'n'. como o a seguir;


    x = 'Nullam facilisis turpis ut placerat dictum; \nnullam auctor finibus ' 
    \   'aliquet.'
    print(x)
    
    Nullam facilisis turpis ut placerat dictum; 
    nullam auctor finibus aliquet.


Em textos que fazem o uso de aspas, seja elas simples ou duplas, devemos 
mesclar o uso durante a atribuição da variável; Se o texto apresenta aspas 
duplas, devemos declarar a variável com aspas simples, em caso de o texto 
possuir aspas simples declaramos a variável com aspas duplas.

    x = "Caixa d' agua"
    y = 'Esse "texto" possui aspas duplas'

Em casos onde o uso dos dois modelos de aspas são necessários no texto, 
devemos utilizar a contra barra (alt+92 em teclados americanos); 
Fazendo dessa forma o próximo caractere será interpretado como parte do 
texto.    

    x = 'Ele "encheu" a caixa d\' agua.'
    print(x)
    
    Ele "encheu" a caixa d' agua.

    OU
    
    x = "Ele \"encheu\" a caixa d' agua."
    print(x)

    Ele "encheu" a caixa d' agua.

Caso seja necessário escrever um texto de múltiplas linhas uma outra forma 
é através do uso de três aspas, seja simples ou duplas, lembrando que a que 
for usada para iniciar a string deve ser usada para fechar;

    
    x = '''    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Phasellus a lacus orci. 
        Sed accumsan tortor ligula, id blandit magna dignissim venenatis. 
    Maecenas consequat risus quis efficitur commodo.'''
    print(x)  
    
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Phasellus a lacus orci. 
        Sed accumsan tortor ligula, id blandit magna dignissim venenatis. 
    Maecenas consequat risus quis efficitur commodo.

Durante o uso do modelo acima notamos que o resultado é apresentado da mesma 
forma que no programa, o que retira a necessidade do uso de comandos 
especiais para quebras de linhas por exemplo.
"""

x = '1234567890'
print(x[::-1])
