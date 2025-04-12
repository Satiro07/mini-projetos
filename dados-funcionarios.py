def menu():
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. Buscar gerentes')
    print('4. Buscar chefes')

def adicionar_funcionario():
    func = {}
    func['nome'] = input('Nome do funcionario: ')
    func['cargo'] = input('Cargo do funcionario: ')
    print(func)
funcionarios = []


while True:
    menu()
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        adicionar_funcionario()