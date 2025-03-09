def menu():
    print('1. Adicionar compra')
    print('2. Editar lista')
    print('3. Excluir')
    print('4. Vizualizar lista')
    print('0. Sair')

def add_produto(produto):
    produtos = []
    produtos.append(produto)
    return produtos

def add_valor(valor):
    valores = []
    valores.append(valor)
    return valores

def add_tipo(tipo):
    tipos = []
    tipos.append(tipo)
    return tipos

geral = []
while True:
    menu()
    esc = input('Escolha a opção que deseja: ')
    if esc == '1':
        while True:
            prod = input('Digite o nome do produto: ')
            valor = float(input('Digite o valor do produto: R$'))
            tipo = input('Digite o tipo do produto: ')
            
            geral.append(add_produto(prod))
            geral.append(add_valor(valor))
            geral.append(add_tipo(tipo))
            continuar = input('Deseja continuar? [s/n] ').lower()
            if continuar == 's':
                continue
            else:
                break
            
    # elif esc == '2':
    # elif esc == '3':
    elif esc == '4':
        ind = 0 # nome produtos
        ind1 = 1 # valores
        ind2 = 2 # tipos
        printar = len(geral) / 3
        print(f'{"produtos":<10} {"valores":<10} {"tipos":<10}')

        for i in range(0, int(printar)):
            
            print(f'{geral[ind][0]:<10} R${geral[ind1][0]:<10} {geral[ind2][0]:<10}')
            ind += 3
            ind1 += 3
            ind2 += 3

    elif esc == '0':
        break