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

lista = []
while True:
    menu()
    esc = input('Escolha uma opção: ')
    if esc == '1':
        continuar = 's'
        while continuar == 's':
            nome = input('Digite o nome do aluno: ').strip()
            matricula = int(input('Digite a matricula do aluno: '))
            lista.append([nome, matricula])
            continuar = input('deseja continuar? [s/n] ')
    elif esc == '2':
        remover = int(input('Digite a matricula do aluno que deseja remover: '))
        for i in range(0, len(lista)):
            if remover == lista[i][1]:
                lista.remove(lista[i])
                break    
    else:
        print(lista)


# nome = 'jose'
# mat = 120
# notas = []

# notas.append('Matematica : 10')
# lista.append([nome, mat, notas])
# nome1 = 'jose'
# mat1 = 120
# lista.append([nome1, mat1])
# print(lista)
# print(len(lista))