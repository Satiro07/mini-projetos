from random import choice
palavras = ['maracuja', 'ninho', 'copo', 'capacete', 'canudo']
sorteio_palavra = choice(palavras)
quantidade_letras = len(sorteio_palavra)
print(sorteio_palavra)
tentativas = 6
palavra = ''
print('_ ' * quantidade_letras)
quant2 = quantidade_letras
while quant2:
    palavra += '_'
    quant2 -= 1
c = 1
palavra[c] = 'a'
print(palavra)
# while True:
    
#     letra_usuario = input('Digite uma letra: ')
#     certo = 0
#     veri = quantidade_letras
#     for i in range(0, veri):
#         if letra_usuario == sorteio_palavra[i]:
#             print('contem a letra')
#             palavra[i] = letra_usuario
#             certo += 1
#         else:
#             palavra += '_ '

#     print(palavra)
#     if certo == 0:
#         print('não tem a palavra')
#         break