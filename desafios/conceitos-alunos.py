""" Objetivo: Criar um sistema de conceito para notas de alunos seguindo a
tabela de referência.

Conceito | Notas
A           De 9,1 a 10,0
A-          De 8,1 a 9,0
B           De 7,1 a 8,0
B-          De 6,1 a 7,0
C           De 5,1 a 6,0
C-          De 4,1 a 5,0
D           De 3,1 a 4,0
D-          De 2,1 a 3,0
E           De 1,1 a 2,0
E-          De 0,0 a 1,0

"""

nota = input('Por favor informe a nota do aluno.\n')
nota = float(nota)

if 9.1 <= nota <= 10.0:
    print('O aluno está com o conceito: A')

if 8.1 <= nota <= 9.0:
    print('O aluno está com o conceito: A-')

if 7.1 <= nota <= 8.0:
    print('O aluno está com o conceito: B')

if 6.1 <= nota <= 7.0:
    print('O aluno está com o conceito: B-')

if 5.1 <= nota <= 6.0:
    print('O aluno está com o conceito: C')

if 4.1 <= nota <= 5.0:
    print('O aluno está com o conceito: C-')

if 3.1 <= nota <= 4.0:
    print('O aluno está com o conceito: D')

if 2.1 <= nota <= 3.0:
    print('O aluno está com o conceito: D-')

if 1.1 <= nota <= 2.0:
    print('O aluno está com o conceito: E')

if 0.0 <= nota <= 1.0:
    print('O aluno está com o conceito: E-')

if nota >= 10.1:
    print('Nota inválida')

if nota <= -0.9:
    print('Nota Inválida')
