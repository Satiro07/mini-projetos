import numpy as np
from random import randint

array = np.zeros((3, 3))
print(f'{array}\n')
jogadas = []
resto = [0, 1, 2, 3, 4, 5, 6, 7, 8]
fim = 1
while True:
    
    escolha_maquina = randint(resto[0],resto[-1])
    while escolha_maquina in jogadas:
        escolha_maquina = randint(resto[0],resto[-1])
    if escolha_maquina not in jogadas:
        jogadas.append(escolha_maquina)
        resto.remove(escolha_maquina)
    
    for i in range(0, 1):
        if escolha_maquina <= 2:
            c = escolha_maquina
            cont = 0
        elif escolha_maquina <= 5:
            c = escolha_maquina-3
            cont = 1
        else:
            c = escolha_maquina-6
            cont = 2
        array[cont][c] = 1
    
    if fim == 5:
        break
    else:
        print(array)
    escolha_jogador = int(input(f'Escolha uma posição {resto}:'))
    if escolha_jogador not in jogadas:
        jogadas.append(escolha_jogador)
        resto.remove(escolha_jogador)

    for y in range(0,1):
        if escolha_jogador <= 2:
            c = escolha_jogador
            cont = 0
        elif escolha_jogador <= 5:
            c = escolha_jogador-3
            cont = 1
        else:
            c = escolha_jogador-6
            cont = 2
        array[cont][c] = 3
    
    
    fim += 1
print(array)