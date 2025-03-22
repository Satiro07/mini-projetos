from random import choice
palavras = ['maracuja', 'ninho', 'copo', 'capacete', 'canudo']
sorteio_palavra = choice(palavras)
quantidade_letras = len(sorteio_palavra)
print(sorteio_palavra)
tentativas = 6
palavra = ''
print('_' * quantidade_letras)
quant2 = quantidade_letras
palavra_cons = ''
cont = 4
palavranova = ''
# print(palavra_cons.replace('b', sorteio_palavra[cont]))
while True:
    palavra_aux = ''
    while quant2:
        palavra += '_'
        quant2 -= 1
    palavra = palavra
    letra_usuario = input('Digite uma letra: ')
    
    veri = quantidade_letras
    for i in range(0, veri):
        if letra_usuario == sorteio_palavra[i]:
            print('contem a letra')
            
            palavra_aux += letra_usuario

        else:
            palavra_aux += '_'

    
    if cont >= 2:
        for i in range(0, veri):
            if palavra_aux[i] != palavra_cons[i]:
                palavranova.replace(palavra_aux[i],palavra_cons[i]) 
            else:
                palavranova.replace(palavra_aux[i],palavra_cons[i]) 
    else:
        palavranova = palavra_aux
        palavra_cons = palavra_aux
    
    
    print(palavra_aux)
    print(palavra_cons)
    print(palavranova)
    cont += 1