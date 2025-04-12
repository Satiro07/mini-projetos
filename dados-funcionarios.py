def menu():
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. Buscar gerentes')
    print('4. Buscar chefes')

def adicionar_funcionario():
    sair = 's'
    while sair != 'n':
        func = {}
        nome = input('Nome do funcionario: ')
        func[nome] = input('Cargo do funcionario: ')
        funcionarios.append(func)
        sair = input('Deseja adicionar outro funcionario? [s/n] ').lower()

def exibir_funcionarios():
    for funcionario in funcionarios:
        for k, v in funcionario.items():
            print(f'nome: {k} - cargo: {v}')
        
def buscar_gerente():
    for funcionario in funcionarios:
        for k, v in funcionario.items():
            if v.lower() == 'chefe':
                print(f'nome: {k} - cargo: {v}')
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
        buscar_gerente()

