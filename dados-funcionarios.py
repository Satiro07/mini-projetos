def menu():
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. listar gerentes')
    print('4. listar chefes')

def adicionar_funcionario():
    sair = 's'
    while sair != 'n':
        func = {}
        nome = input('Nome do funcionario: ')
        func[nome] = input('Cargo do funcionario: ')
        funcionarios.append(func)
        sair = input('Deseja adicionar outro funcionario? [s/n] ').lower()

def exibir_funcionarios():
    print('Funcionarios cadastrados:')
    print()
    for funcionario in funcionarios:
        for k, v in funcionario.items():
            print(f'Nome: {k} - Cargo: {v}')
    print()
        
def listar_gerente():
    print('Gerentes cadastrados: ')
    print()
    for funcionario in funcionarios:
        for k, v in funcionario.items():
            if v.lower() == 'gerente':
                print(f'Nome: {k} - Cargo: {v}')
    print()

def listar_chefe():
    print('Chefes cadastrados:')
    print()
    for funcionario in funcionarios:
        for k, v in funcionario.items():
            if v.lower() == 'chefe':
                print(f'Nome: {k} - Cargo: {v}')
    print()
funcionarios = []

while True:
    menu()
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        adicionar_funcionario()
        print(funcionarios)
    elif escolha == 2:
        exibir_funcionarios()
    elif escolha == 3:
        listar_gerente()
    elif escolha == 4:
        listar_chefe()

