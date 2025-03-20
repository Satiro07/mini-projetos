def menu():
    print(f'{"Menu":-^20}')
    print('1. Adicionar novo contato')
    print('2. Lista de todos os contatos')
    print('3. Pesquisar contato pelo nome')
    print('4. Sair do Gerenciador de Contatos')

def adicionar_contatos(nome, numero):
    with open(arquivo_caminho, 'w') as arquivo:
        arquivo.write(nome)
        arquivo.write(numero)
    return arquivo_caminho

def add_contatos2(nome, numero):
    with open(arquivo_caminho, 'a') as arquivo:
        arquivo.write(nome)
        arquivo.write(numero)
    return arquivo_caminho

import os
import shutil

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'
nome_pasta = input('Nome da pasta que deseja criar: ')

nome_arquivo = input('Nome do arquivo (escreva com a extensão ".txt"): ')

arquivo_caminho = os.path.join(desktop, nome_arquivo)

c = 0
while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        if c == 0:
            nome_contato = input('Nome do contato que deseja adicionar: ') + ' '
            numero_contato = input('Número do contato que deseja adcionar: (ex:9999-9999) ') + ' '
            adicionar_contatos(nome_contato, numero_contato)  
            print(f'Contato {nome_contato}adicionado com sucesso!')
        else: 
            nome_contato = input('Nome do contato que deseja adicionar: ') + ' '
            numero_contato = input('Número do contato que deseja adcionar: (ex:9999-9999) ') + ' '
            add_contatos2(nome_contato, numero_contato)  
            print(f'Contato {nome_contato}adicionado com sucesso!')
        c += 1

    elif escolha == '2':
        if c == 0:
            print('Você precisa adicionar pelo menos um contato:')
        else:
            print(f'{"SEUS CONTATOS ":-^20}')
            print('')
            with open(arquivo_caminho, 'r') as arquivo:
                lista = arquivo.read()
                lista = lista.split(' ')
                lista.pop()
            c = 0
            for i in range(0, int(len(lista)/2)):
                print(f'Nome: {lista[c]}, telefone: {lista[c+1]}')
                c += 2

    elif escolha == '3':
        nome = input('Nome do contato: ')
        with open(arquivo_caminho, 'r') as arquivo:
            lista = arquivo.read()
            lista = lista.split(' ')
            lista.pop()
        c = 0
        t = False
        while c <= int(len(lista)/2):
            if nome.lower() == lista[c].lower():
                print('Contato encontrado')
                print(f'Nome: {lista[c]}, telefone: {lista[c+1]}')
                t = True
                break
            c += 2
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