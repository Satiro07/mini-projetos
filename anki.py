def menu():
    print('Opções:')
    print('1 - Criar baralho')
    print('2 - Adicionar baralho')
    print('3 - Ver baralho')
    print('4 - Editar baralho')
    print('5 - Sair')



lista = []
dic = {}
while True:
    
    lista = []
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        nome_baralho = input('Nome do baralho: ')
        dic[nome_baralho] = ''
        print(dic)
    elif escolha == '2':
        print('Nome baralhos: ')
        for k in dic.keys():
            print(k)
        escolha_baralho = input('Nome do baralho que deseja adicionar cartas: ')
        if escolha_baralho in dic:
            frente = input('Pergunta: ')
            verso = input('Resposta: ')
            dic1 = {}
            for k in dic.keys():
                if escolha_baralho == k:
                    lista.append([frente, verso])
                    dic = lista
                    
        else:
            print('Baralho não encontrado')
    elif escolha == '3':
        c = 0
        c1 = 1
        for pergunta in lista:
            for valor in pergunta.values():
                for v in valor.values():
                    print(f'Pergunta: {v[c]}, Resposta: {v[c1]}')
                    c += 2
                    c1 += 2
    print(dic)