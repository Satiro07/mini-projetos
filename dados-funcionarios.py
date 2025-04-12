def menu():
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. Buscar gerentes')
    print('4. Buscar chefes')

def adicionar_funcionario():
    func = {}
    sair = 's'
    while sair != 'n':
        func['nome'] = input('Nome do funcionario: ')
        func['cargo'] = input('Cargo do funcionario: ')
        funcionarios.append([func])
        sair = input('Deseja adicionar outro funcionario? [s/n]').lower()

def exibir_funcionarios():
    for funcionario in funcionarios[0]:
        for k, v in funcionario.items():
            print(f'{k} = {v}')
funcionarios = []


while True:
    menu()
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        adicionar_funcionario()
        print(funcionarios)
    elif escolha == 2:
        exibir_funcionarios()
