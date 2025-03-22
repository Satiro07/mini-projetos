from random import choice
palavras = ['maracuja', 'ninho', 'copo', 'capacete', 'canudo']
sorteio_palavra = choice(palavras)
quantidade_letras = len(sorteio_palavra)
print(sorteio_palavra)
tentativas = 6
palavra = ''
print('_ ' * quantidade_letras)
quant2 = quantidade_letras

while True:
    while quant2:
        palavra += '_ '
        quant2 -= 1
    palavra1 = palavra
    letra_usuario = input('Digite uma letra: ')
    certo = 0
    veri = quantidade_letras
    for i in range(0, veri):
        if letra_usuario == sorteio_palavra[i]:
            print('contem a letra')
            palavra = letra_usuario + palavra
            certo += 1
            
        else:
            palavra = '_ ' + palavra
        palavra = palavra - palavra1
    print(palavra)
    if certo == 0:
        print('não tem a palavra')
        break