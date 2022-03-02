def dias_da_semana(dia):
    dias = {
        1: 'domingo',
        2: 'segunda',
        3: 'terça',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sábado'
    }
    return dias.get(dia)


if __name__ == '__main__':

    while True:
        try:
            entrada = input('Insira o dia da semana\n')
            entrada = int(entrada)
            if entrada in range(2, 7):
                print(f'O dia escolhido foi o "{dias_da_semana(entrada)}",'
                      f' ele é um dia de semana.')
                continue
            elif entrada == 1 or entrada == 7:
                print(
                    f'O dia escolhido foi o "{dias_da_semana(entrada)}", '
                    f'ele é um dia do final de semana.')
                continue
            else:
                print('Data inválida')
                break
        except ValueError:
            print('Erro')
            break
