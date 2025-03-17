def menu():
    print('1. adicionar aluno')
    print('2. remover aluno')
    print('3. boletim')
    print('4. editar')

def menu_editar():
    print('O que deseja editar?')
    print('1. Nome do aluno')
    print('2. Nome da matéria')
    
lista = []
while True:
    menu()
    esc = input('Escolha uma opção: ')
    if esc == '1':
        continuar = 's'
        while continuar == 's':
            nome = input('Digite o nome do aluno: ').strip()
            matricula = int(input('Digite a matricula do aluno: '))
            materia_nota = []
            materia_nota.append(nome)
            materia_nota.append(matricula)
            cont = 's'
            while cont == 's':
                mat = []
                materia = input('Nome da matéria: ')
                print('Digite as notas [digite um número menor de 0 ou maior de 10 para sair]')
                nota = 1
                mat.append(materia)
                while 0 <= nota <= 10:
                    nota = float(input('Digite a nota:'))
                    if 0 <= nota <= 10:
                        mat.append(nota)
                materia_nota.append(mat)
                cont = input('deseja adicionar outra máteria? [s/n] ')
            lista.append(materia_nota)
            continuar = input('deseja adicionar outro aluno? [s/n] ')
    elif esc == '2':
        remover = int(input('Digite a matricula do aluno que deseja remover: '))
        for i in range(0, len(lista)):
            if remover == lista[i][1]:
                lista.remove(lista[i])
                break   
    elif esc == '3':
        for aluno in lista:
            print(aluno)
    elif esc == '4':
        menu_editar()
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            if not lista:
                print('Precisa add algum aluno!')
            else:
                while True:
                    v = False
                    chave_matricula = int(input('Digite a mátricula do aluno: '))
                    for i in range(0, len(lista)):
                        if chave_matricula == lista[i][1]:
                            editar = input('Novo nome: ')
                            lista[i][0] = editar
                            v = True
                    if v == True:
                        print('Nome foi mudado com sucesso')
                        break
                    else:
                        print('Matricula não encontrada')
        elif escolha == '2':
            if not lista:
                print('Precisa add algum aluno!')
            else:
                
                while True:
                    chave_matricula = int(input('Digite a mátricula do aluno: '))
                    two = 2
                    
                    lei = len(lista)
                    for i in range(0, lei):
                        print(lista[0][two][0])
                        two += 1
                        if lista[0][two][0]:
                            continue
                        else:
                            break
                    for i in range(0, len(lista)):
                        if chave_matricula == lista[i][1]:
                            nome_velho = input('Nome que deseja mudar: ')
                            two = 2
                            for i in range(0, len(lista)):
                                print(lista[i][two][0])
                                if nome_velho == lista[i][two][0]:
                                    editar = input('Novo nome da materia: ')
                                    lista[i][two][0] = editar
                                two += 1
                            v = True
                    if v == True:
                        print('Nome da materia foi mudado com sucesso')
                        break
                    else:
                        print('Matricula não encontrada')
                    
    else:
        break



# notas = ['Jose', '7', ['Mat', 1, 2, 4], ['hist', 10], ['geo', 10, 8]]



# two = 2
# lei = len(notas)
# for i in range(0, lei):
#     print(notas[two][0])
    
#     if lei - 1 == two:
#         break
#     two += 1
# print(len(notas))