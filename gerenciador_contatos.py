def menu():
    print(f'{"Menu":-^20}')
    print('1. Adicionar novo contato')
    print('2. Lista de todos os contatos')
    print('3. Pesquisar contato pelo nome')
    print('4. Sair do Gerenciador de Contatos')

def adicionar_contatos(nome, numero):
    with open(arquivo_caminho, 'a') as arquivo:
        arquivo.write(f'{nome};{numero}\n')    
    return arquivo_caminho


import os
import shutil

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'

nome_pasta = input('Nome da pasta que deseja criar: ')

nome_arquivo = input('Nome do arquivo (escreva com a extensão ".txt"): ')

arquivo_caminho = os.path.join(desktop, nome_arquivo)

if not os.path.exists(arquivo_caminho):
    with open(arquivo_caminho, 'w') as arquivo:
        pass

c = 0
while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        nome_contato = input('Nome do contato que deseja adicionar: ')
        numero_contato = input('Número do contato que deseja adcionar: (ex:9999-9999) ')
        adicionar_contatos(nome_contato, numero_contato)  
        print(f'Contato {nome_contato}adicionado com sucesso!')
        c += 1

    elif escolha == '2':
        if c == 0:
            print('Você precisa adicionar pelo menos um contato:')
        else:
            print(f'{"SEUS CONTATOS ":-^20}')
            print('')
            with open(arquivo_caminho, 'r') as arquivo:
                for linha in arquivo:
                    nome, numero = linha.strip().split(';')
                    print(f'Nome: {nome} - Telefone: {numero}')

    elif escolha == '3':
        nome_cont = input('Nome do contato: ')
        t = False
        with open(arquivo_caminho, 'r') as arquivo:
            for linha in arquivo:
                nome, numero = linha.strip().split(';')
                if nome_cont.lower() == nome.lower():
                    print('Contato encontrado')
                    print(f'Nome: {nome} - Telefone: {numero}')
                    t = True
                    break
        if t == False:
            print(f'Contato {nome} não encontrado')
            
    elif escolha == '4':
        print('saindo...')
        break
    else:
        print('Escolha uma opção válida')

if os.path.exists(arquivo_caminho):
    pasta = os.path.join(desktop, nome_pasta)
    os.makedirs(pasta, exist_ok=True)

    pasta = os.path.join(pasta, nome_arquivo)
    shutil.move(arquivo_caminho, pasta)
    print(f'Arquivo movido para: {pasta}')
else:
    print(f'Nenhum arquivo de contatos foi criado')