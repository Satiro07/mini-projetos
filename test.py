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

cont = len(palavra[0])
pala_comp = ''
num = 0
fim = []
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
                if len(letras) == len(palavra[0]):
                    letras.remove(letras[c])
                    letras.insert(c, letra)
                else:
                    letras.append(letra)
                    letras.count(letra)
            else:
                if len(letras) == len(palavra[0]):
                    if letra != pala_comp[c]:
                        letra.replace(pala_comp[c], letra)
                else:
                    letras.append('_')
            c += 1
            quant -= 1
    for letra in letras:
        print(letra, end=' ')
    print()
    
    for i in range(0, cont):
        pala_comp = letras
    print(pala_comp)
    letras = pala_comp