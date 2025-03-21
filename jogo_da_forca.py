from random import choice
palavras = ['maracuja', 'ninho', 'copo', 'capacete', 'canudo']
sorteio_palavra = choice(palavras)
quantidade_letras = len(sorteio_palavra)
print(sorteio_palavra)
tentativas = 6
quantidade_letras2 = quantidade_letras
while True:
    letra = ''
    barra = '_'
    while quantidade_letras2:
        print(barra, end=' ')
        quantidade_letras2 -= 1
    print()
    letra_usuario = input('Digite uma letra: ')
    certo = 0
    veri = quantidade_letras
    for i in range(0, veri):
        if letra_usuario == sorteio_palavra[i]:
            print('contem a palavra')
            certo += 1

    if certo == 0:
        print('não tem a palavra')
        break