# geral = []
# produto = []
# prod = 'feijao'
# produto.append(prod)
# geral.append(produto)

# tipos = []
# tipo = 'kilo'
# tipos.append(tipo)
# geral.append(tipos)

# valor = []
# val = 5
# valor.append(val)
# geral.append(valor)
# ind = 0 # nome produtos
# ind1 = 1 # valores
# ind2 = 2 # tipos
# print(len(geral))
# print(geral)


# geral = [[5, 4], [4], [3]]
# geral[0][1] = 3
# print(geral)


letras = []
palavra = ['ninho']


pala_comp = ''
while True:
    c = 0
    letra = input('Letra: ')
    quant = (len(palavra))
    if letra not in palavra[0]:
        print('erro')
    elif letra in letras:
        print('Letra ja adicionada')
    else:
        while quant > 0 or c < len(palavra[0]):
            
            if letra == palavra[0][c]:
                letras.append(letra)
                letras.count(letra)
            c += 1
            quant -= 1
    print(letras)
    print(palavra[0][1])
    if letra == 's':
        for i in range(0, quant):
            pala_comp += letras[0][i]
        print(pala_comp)
        break