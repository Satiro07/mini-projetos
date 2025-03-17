# Crie um programa que permita ao usuário registrar
# informações de alunos incluindo nome, matrícula e
# notas em várias disciplinas. Use uma listra aninhada
# para representar os alunos, onde cada aluno é uma
# lista com três elementos: nome, matrícula e uma
# lista de notas. O programa deve permitir adicionar
# novos alunos e removê-los pelo número de matrícula.

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
                    c = 0
                    two = 2
                    v = False
                    chave_matricula = int(input('Digite a mátricula do aluno: '))
                    
                    while c < len(lista):
                        print(f'{c+1}. {lista[0][two][0]}')
                        c += 1
                        two += 1
                    for i in range(0, len(lista)):
                        if chave_matricula == lista[i][1]:
                            mudar_mate = input('Nome da materia que deseja editar: ')
                            if mudar_mate == lista[i][2][0]:
                                editar = input('Novo nome da matéria: ')
                                lista[i][2][0] = editar
                                v = True
                    if v == True:
                        print('Nome da materia foi mudado com sucesso')
                        break
                    else:
                        print('Matricula não encontrada')

                    
                
                
                    
                

            
    else:
        break



# notas = []
# notasa = 'matematica: 10'

# materia_nota = []
# nome1 = 'jose'
# mat1 = 120
# materia_nota.append(notasa)
# lista.append([nome1, mat1, materia_nota])




# print(lista)
# print(len(lista))