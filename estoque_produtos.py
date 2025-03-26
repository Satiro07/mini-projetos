def menu():
    print('Opções:')
    print('1 - Adicionar produto')
    print('2 - Atualizar quantidade')
    print('3 - Remover produto')
    print('4 - Mostrar estoque')
    print('5 - Sair')

def add_produto(quantidade, preco):
    lista = []
    lista.append([quantidade, preco])
    return lista

dic = {}

while True:
    geral = []
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        continuar = 's'
        while continuar != 'n':

            nome_produto = input('Nome do produto: ')
            quantidade = int(input('Quantidade: '))
            preco = float(input('Preço unitário: '))
            preco_total = quantidade * preco
            dic[nome_produto] = quantidade, preco_total
            continuar = input('Deseja adicionar mais produtos? [s/n]').lower()
        break
for k, v in dic.items():
    print(f'{k} - Quantidade {v[0]} - Preço total {v[1]:.2f}')
    

# \n