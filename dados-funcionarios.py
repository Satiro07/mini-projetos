
def menu(func):
    print('-'*40)
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. listar gerentes')
    print('4. listar chefes')
    print('5. Remover funcionário')
    escolha = int(input('Escolha uma opção: '))
    return escolha

def adicionar_funcionario(cod):
    func = {}
    print('-'*40)
    func['Nome'] = input('Nome do funcionario: ').strip()
    func['Cargo'] = input('Cargo do funcionario: ').lower()
    while func['Nome'] == '' or func['Cargo'] == '':
        print('Nenhum campo pode ficar vazio!')
        if func['Nome'] == '':
            func['Nome'] = input('Nome do funcionario: ').strip()
        if func['Cargo'] == '':
            func['Cargo'] = input('Cargo do funcionario: ').lower()
    func['ID'] = cod
    return funcionarios.append(func)

def exibir_funcionarios():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('-'*40)
        print('Funcionarios cadastrados:')
        print()
        for funcionario in funcionarios:
            for k, v in funcionario.items():
                print(f'{k}: {v}')
            print('-'*40)
    print()
        
def listar_gerente():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('Gerentes cadastrados: ')
        print()
        verificacao = False
        print('-'*40)
        for funcionario in funcionarios:
            if funcionario['Cargo'] == 'gerente':
                for k, v in funcionario.items():
                    print(f'{k}: {v}')
                    verificacao = True
                print('-'*40)
        if verificacao == False:
            print('Nenhum gerente cadastrado!')
    print()

def listar_chefe():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('-'*40)
        print('Chefes cadastrados:')
        print()
        verificacao = False
        for funcionario in funcionarios:
            if funcionario['Cargo'] == 'chefe':
                for k, v in funcionario.items():
                    print(f'{k}: {v}')
                    verificacao = True
                print('-'*40)
        if verificacao == False:
            print('Nenhum chefe cadastrado!')
    print()

def remover_funcionario():
    senha = 1234
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('-'*40)
        for funcionario in funcionarios:
            for k, v in funcionario.items():
                print(f'{k}: {v}')
            print('-'*40)
        print()
        print('Remova pelo ID!')
        coder = int(input('Digite o ID do funcionário que deseja remover: '))
        verificacao = False
        for funcionario in funcionarios:
            if coder == funcionario['ID']:
                verificacao = True
                senha_verificação = int(input('Digite a senha para remover funcionário: '))
                tentativas = 0
                if senha == senha_verificação:
                    funcionarios.remove(funcionario)
                    print()
                    print(f"Funcionario(a) {funcionario['Nome'].upper()}, removido com sucesso!")
                else:
                    while senha_verificação != senha and tentativas != 3:
                        print('Senha incorreta!')
                        senha_verificação = int(input('Digite a senha para remover funcionário: '))
                        tentativas += 1
                        if tentativas == 3:
                            print('Limite de tentativas atingida')
                        if senha == senha_verificação:
                            funcionarios.remove(funcionario)
                            print()
                            print(f"Funcionario(a) {funcionario['Nome'].upper()}, removido com sucesso!")
        if verificacao == False:
            print(f'Nenhum funcionário com o ID: {coder}')
            
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
    elif escolha == 5:
        remover_funcionario()
    else:
        print('-'*40)
        print('Erro! Escolha uma opção válida!')