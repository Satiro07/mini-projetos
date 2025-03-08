def menu():
    print('1. Adicionar compra')
    print('2. Editar lista')
    print('3. Excluir')
    print('4. Vizualizar lista')
    print('0. Sair')

def add_produto(produto, valor, tipo):
    produtos = []
    produtos.append(produto)
    valores = []
    valores.append(valor)
    tipos = []
    tipos.append(tipo)
    
    return produtos, valores, tipos

while True:
    geral = []
    menu()
    esc = input('Escolha a opção que dedseja: ')
    if esc == '1':
        continuar = 's'
        while continuar != 'n':
            prod = input('Digite o nome do produto: ')
            valor = float(input('Digite o valor do produto: R$'))
            tipo = input('Digite o tipo do produto: ')
            prods = add_produto(prod, valor, tipo)
            geral.append(prods)
            continuar = input('Deseja continuar? [s/n] ').lower()
            if continuar == 's':
                continue
            
               
            
    # elif esc == '2':
    # elif esc == '3':
    elif esc == '4':
        print(geral)
    elif esc == '0':
        break