def menu(func):
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. listar gerentes')
    print('4. listar chefes')
    print('5. Remover funcionário')
    escolha = int(input('Escolha uma opção: '))
    return escolha

def adicionar_funcionario(cod):
    func = {}
    func['Nome'] = input('Nome do funcionario: ').strip()
    func['Cargo'] = input('Cargo do funcionario: ').lower()
    while func['Nome'] == '' or func['Cargo'] == '':
        print('Nenhum campo pode ficar vazio!')
        func['Nome'] = input('Nome do funcionario: ').strip()
        func['Cargo'] = input('Cargo do funcionario: ').lower()
    func['ID'] = cod
    return funcionarios.append(func)

def exibir_funcionarios():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('Funcionarios cadastrados:')
        print()
        for funcionario in funcionarios:
            for k, v in funcionario.items():
                print(f'{k}: {v}',end=(' - '))
            print()
    print()
        
def listar_gerente():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('Gerentes cadastrados: ')
        print()
        verificacao = False
        for funcionario in funcionarios:
            if funcionario['Cargo'] == 'gerente':
                for k, v in funcionario.items():
                    print(f'{k}: {v}',end=(' - '))
                    verificacao = True
        if verificacao == False:
            print('Nenhum gerente cadastrado!')
    print()

def listar_chefe():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('Chefes cadastrados:')
        print()
        verificacao = False
        for funcionario in funcionarios:
            if funcionario['Cargo'] == 'chefe':
                for k, v in funcionario.items():
                    print(f'{k}: {v}',end=(' - '))
                    verificacao = True
        if verificacao == False:
            print('Nenhum chefe cadastrado!')
    print()

funcionarios = []
cod = 1
while True:
    escolha = menu(funcionarios)
    if escolha == 1:
        sair = 's'
        while sair != 'n':
            opcao = adicionar_funcionario(cod)
            cod += 1
            sair = input('Deseja adicionar outro funcionario? [s/n] ').lower()
    elif escolha == 2:
        exibir_funcionarios()
    elif escolha == 3:
        listar_gerente()
    elif escolha == 4:
        listar_chefe()
    else:
        print('Erro! Escolha uma opção válida!')


