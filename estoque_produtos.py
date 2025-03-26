def menu():
    print('Opções:')
    print('1 - Adicionar produto')
    print('2 - Atualizar quantidade')
    print('3 - Remover produto')
    print('4 - Mostrar estoque')
    print('5 - Sair')

dic = {}
while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        continuar = 's'
        while continuar != 'n':

            nome_produto = input('Nome do produto: ')
            quantidade = int(input('Quantidade: '))
            preco = float(input('Preço unitário: '))
            preco_total = quantidade * preco
            dic[nome_produto] = [quantidade, preco_total, preco]
            continuar = input('Deseja adicionar mais produtos? [s/n] ').lower()
    elif escolha == '2':
        nome = input('Nome do produto para atualizar: ')
        if nome in dic:
            nova_quant = int(input('Nova quantidade: '))
            for k, v in dic.items():
                if k == nome:
                    v[0] = nova_quant
                    v[1] = v[0] * v[2]
        else:
            print('Produto não encontrado! Verifique acentos!!')
    elif escolha == '3':
        nome = input('Nome do produto que deseja remover: ')
        if nome in dic:
            del dic[nome]
    elif escolha == '4':
        if len(dic) != 0:
            for k, v in dic.items():
                print(f'{k} - Quantidade: {v[0]} - Preço total: R${v[1]:.2f}')
        else:
            print('Você precisa adicionar produtos primeiro!')
            
    elif escolha == '5':
        break
    else:
        print('Escolha uma opção válida!')
    

# \n