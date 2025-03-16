def menu():
    print('1. Adicionar compra')
    print('2. Editar lista')
    print('3. Excluir')
    print('4. Vizualizar lista')
    print('0. Sair')

def menu_2():
    print('1. produto')
    print('2. valor')
    print('3. tipo')

geral = []
while True:
    menu()
    esc = input('Escolha a opção que deseja: ')
    if esc == '1':
        while True:
            prod = input('Digite o nome do produto: ')
            valor = float(input('Digite o valor do produto: R$'))
            tipo = input('Digite o tipo do produto: ')
            geral.append([prod, valor, tipo])
            continuar = input('Deseja continuar? [s/n] ').lower()
            if continuar == 's':
                continue
            else:
                break

    elif esc == '2':
        if not geral:
            print('Você precisa adicionar alimentos!')
        else:
            print('O que deseja editar?')
            menu_2()
            escolha = input('Escolha: ')
            c = 0

            if escolha == '1':
                for produto in geral:
                    print(f'{c}. {produto[0]}')
                    c += 1
                indice = c+1
                while indice >= c:
                    indice = int(input('Indice do produto que deseja editar: '))
                esc_prod = input('Novo nome do produto: ')
                geral[indice][0] = esc_prod

            elif escolha == '2':
                for produto in geral:
                    print(f'{c}. {produto[0]:<10} R${produto[1]:<10}')
                    c += 1
                indice = c+1
                while indice >= c:
                    indice = int(input('Indice do valor que deseja editar: '))
                esc_prod = input('Novo valor: ')
                geral[indice][1] = esc_prod

            elif escolha == '3':
                for produto in geral:
                    print(f'{c}. {produto[0]:<10} R${produto[1]:<10} {produto[2]:<10}')
                    c += 1
                indice = c+1
                while indice >= c:
                    indice = int(input('Indice do tipo que deseja editar: '))
                esc_prod = input('Novo tipo: ')
                geral[indice][2] = esc_prod

    elif esc == '3':
        c = 0
        for produto in geral:
            print(f'{c}. {produto[0]}')
            c += 1
        excluir = c+1
        while excluir >= c:
            excluir = int(input('Qual indice do produto que voce quer excluir? '))
        geral.remove(geral[excluir])
    elif esc == '4':      
        print(f'{"produtos":<10} {"valores":<10} {"tipos":<10}')
        for produto in geral:
            print(f'{produto[0]:<10} R${produto[1]:<10} {produto[2]:<10}')
    elif esc == '0':
        break
    else:
        continue