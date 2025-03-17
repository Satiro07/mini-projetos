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
                    nota = int(input('Digite a nota:'))
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

    else:
        print(lista)
        print(len(lista))



# notas = []
# notasa = 'matematica: 10'

# materia_nota = []
# nome1 = 'jose'
# mat1 = 120
# materia_nota.append(notasa)
# lista.append([nome1, mat1, materia_nota])




# print(lista)
# print(len(lista))