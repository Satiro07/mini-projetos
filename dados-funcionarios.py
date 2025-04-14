from time import sleep

from datetime import datetime
data_hora = datetime.now()
data_registro = data_hora.strftime("%d/%m/%Y, Horário: %H:%M:%S")

def menu(func):
    print('-'*40)
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. listar gerentes')
    print('4. listar chefes')
    print('5. Remover funcionário')
    print('6. Editar funcionário')
    print('7. Sair do programa')
    escolha = input('Escolha uma opção: ')
    return escolha

def adicionar_funcionario(cod):
    func = {}
    print('-'*40)
    func['Nome'] = input('Nome do funcionario: ').strip()
    func['Cargo'] = input('Cargo do funcionario: ').lower()
    dia = input('Dia em que nasceu: ')
    mes = input('Mês em que nasceu: [01, 02...] ')
    ano = input('Ano em que nasceu: [2000, 2001...] ')

    while func['Nome'] == '' or func['Cargo'] == '' or dia == '' or mes == '' or ano == '':
        print('Nenhum campo pode ficar vazio!')
        if func['Nome'] == '':
            func['Nome'] = input('Nome do funcionario: ').strip()
        if func['Cargo'] == '':
            func['Cargo'] = input('Cargo do funcionario: ').lower()
        if dia  == '':
            dia = input('Dia em que nasceu: ')
        if mes == '':
            mes = input('Mês em que nasceu: [01, 02...] ')
        if ano == '':
            ano = input('Ano em que nasceu: [2000, 2001...] ')
    func['ID'] = cod
    func['Data de Registro'] = data_registro
    func['Data de nascimento'] = f'{dia}/' + f'{mes}/' + f'{ano}'
    print('-'*40)
    print('Funcionário adicionado com sucesso!')
    print()
    for k, v in func.items():
        print(f'{k}: {v}')
    print('-'*40)
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


def remover_funcionario(senha):
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
        coder = 0
        while coder != funcionario['ID']:
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
                        break
                    else:
                        while senha_verificação != senha and tentativas != 3:
                            print('Senha incorreta!')
                            senha_verificação = int(input('Digite a senha para remover funcionário: '))
                            tentativas += 1
                            if tentativas == 3:
                                print('Limite de tentativas atingida')
                                break
                            if senha == senha_verificação:
                                funcionarios.remove(funcionario)
                                print()
                                print(f"Funcionario(a) {funcionario['Nome'].upper()}, removido com sucesso!")
                                break
            if verificacao == False:
                print(f'Nenhum funcionário com o ID: {coder}')

def menu_edicao(func):
    print('O que deseja editar? ')
    print('1. Nome')
    print('2. Cargo')
    print('3. Data de nascimento')
    escolha_opcao = input('Escolha uma opção: ')
    return escolha_opcao

def editar_nome_cargo_data_nasc(opcao, senha):
    print('-'*40)
    for funcionario in funcionarios:
        for k, v in funcionario.items():
            print(f'{k}: {v}')
        print('-'*40)
    print()
    coder = 0
    while coder != funcionario['ID']:
        coder = int(input('Digite o ID do funcionário que deseja remover: '))
        verificacao = False
        for funcionario in funcionarios:
            if coder == funcionario['ID']:
                verificacao = True
                if opcao == '1':
                    senha_verificação = int(input('Digite a senha para mudar o nome do funcionário: '))
                    tentativas = 0
                    nome_antigo = funcionario['Nome']
                    if senha == senha_verificação:
                        novo_nome = input('Nome do funcionário atualizado: ')
                        funcionario['Nome'] = novo_nome
                        print()
                        print('Alteração feita com sucesso!')
                        print()
                        print(f'{nome_antigo} ---> {novo_nome}')
                    else:
                        while senha_verificação != senha and tentativas != 3:
                            print('Senha incorreta!')
                            senha_verificação = int(input('Digite a senha para mudar o nome do funcionário: '))
                            tentativas += 1
                            if tentativas == 3:
                                print('Limite de tentativas atingida')
                            if senha == senha_verificação:
                                novo_nome = input('Nome do funcionário atualizado: ')
                                funcionario['Nome'] = novo_nome
                                print()
                                print('Alteração feita com sucesso!')
                                print()
                                print(f'{nome_antigo} ---> {novo_nome}')
                elif opcao == '2':
                    senha_verificação = int(input('Digite a senha para mudar o cargo do funcionário: '))
                    tentativas = 0
                    cargo_antigo = funcionario['Cargo']
                    if senha == senha_verificação:
                        novo_cargo = input(f'Nome do cargo do funcionário {funcionario["Nome"]} atualizado: ').lower()
                        funcionario['Cargo'] = novo_cargo
                        print()
                        print('Alteração feita com sucesso!')
                        print()
                        print(f'{cargo_antigo} ---> {novo_cargo}')
                    else:
                        while senha_verificação != senha and tentativas != 3:
                            print('Senha incorreta!')
                            senha_verificação = int(input('Digite a senha para mudar o cargo do funcionário: '))
                            tentativas += 1
                            if tentativas == 3:
                                print('Limite de tentativas atingida')
                            if senha == senha_verificação:
                                novo_cargo = input(f'Nome do cargo do funcionário {funcionario["Nome"]} atualizado: ').lower()
                                funcionario['Cargo'] = novo_cargo
                                print()
                                print('Alteração feita com sucesso!')
                                print()
                                print(f'{cargo_antigo} ---> {novo_cargo}')
                elif opcao == '3':
                    senha_verificação = int(input('Digite a senha para mudar a data de nascimento do funcionário: '))
                    tentativas = 0
                    data_antiga = funcionario['Data de nascimento']
                    if senha == senha_verificação:
                        dia = input('Dia em que nasceu: ')
                        mes = input('Mês em que nasceu: [01, 02...] ')
                        ano = input('Ano em que nasceu: [2000, 2001...] ')
                        nova_data = f'{dia}/' + f'{mes}/' + f'{ano}'
                        funcionario['Data de nascimento'] = nova_data
                        print()
                        print('Alteração feita com sucesso!')
                        print()
                        print(f'{data_antiga} ---> {nova_data}')
                    else:
                        while senha_verificação != senha and tentativas != 3:
                            print('Senha incorreta!')
                            senha_verificação = int(input('Digite a senha para mudar o cargo do funcionário: '))
                            tentativas += 1
                            if tentativas == 3:
                                print('Limite de tentativas atingida')
                            if senha == senha_verificação:
                                dia = input('Dia em que nasceu: ')
                                mes = input('Mês em que nasceu: [01, 02...] ')
                                ano = input('Ano em que nasceu: [2000, 2001...] ')
                                nova_data = f'{dia}/' + f'{mes}/' + f'{ano}'
                                funcionario['Data de nascimento'] = nova_data
                                print()
                                print('Alteração feita com sucesso!')
                                print()
                                print(f'{data_antiga} ---> {nova_data}')

        if verificacao == False:
            print(f'Nenhum funcionário com o ID: {coder}')
        print()

def editar_informações():
    if not funcionarios:
        print()
        print('Nenhum funcionário adicionado!')
    else:
        print('-'*40)
        escolha_opcao = menu_edicao(funcionarios)
        while escolha_opcao != '1' and escolha_opcao != '2' and escolha_opcao != '3':
            escolha_opcao = menu_edicao(funcionarios)
        if escolha_opcao == '1':
            editar = editar_nome_cargo_data_nasc(escolha_opcao, senha)
        elif escolha_opcao == '2':
            editar = editar_nome_cargo_data_nasc(escolha_opcao, senha)
        elif escolha_opcao == '3':
            editar = editar_nome_cargo_data_nasc(escolha_opcao, senha)
        
funcionarios = []
cod = 1
senha = 1234

while True:
    escolha = menu(funcionarios)
    if escolha == '1':
        sair = 's'
        while sair != 'n':
            opcao = adicionar_funcionario(cod)
            cod += 1
            sair = input('Deseja adicionar outro funcionario? [s/n] ').lower()
    elif escolha == '2':
        exibir_funcionarios()
    elif escolha == '3':
        listar_gerente()
    elif escolha == '4':
        listar_chefe()
    elif escolha == '5':
        remover_funcionario(senha)
    elif escolha == '6':
        editar_informações()
    elif escolha == '7':
        finalizando = 'Saindo.'
        for i in range(0, 3):
            print(finalizando)
            sleep(1)
            finalizando += '.'
        print('Fim do programa')
        break
    else:
        print('-'*40)
        print('Erro! Escolha uma opção válida!')