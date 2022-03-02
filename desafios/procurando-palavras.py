PALAVRAS_PROIBIRAS = ('futebol', 'religião', 'política')
frases = ['João gosta de futebol e política', 'A praia é divertida']

# Para cada frase na lista
for frase in frases:
    # Para cada palavra na frase em minusculo separe
    for palavra in frase.lower().split():
        # se a palavra estiver na lista proibida
        if palavra in PALAVRAS_PROIBIRAS:
            print('O texto possui pelo menos uma palavra proibida:', palavra)
            achou = True
            break
    # Se não achar
    else:
        print('Frase autorizada:', frase)
