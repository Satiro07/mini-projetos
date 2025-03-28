def menu():
    print('Opções:')
    print('1 - Criar baralho')
    print('2 - Adicionar baralho')
    print('3 - Ver baralho')
    print('4 - Editar baralho')
    print('5 - Sair')



dic = {}

while True:
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