categorias = []
def adicionar_categoria():
    esc = 's'
    while esc != 'n':
        nome_categoria = input('Nome da categoria: ')
        if nome_categoria not in categorias:
            categorias.append([nome_categoria, []])
            print(f'Categoria {nome_categoria} adicionada com sucesso!')
        else:
            print('Categoria já esta adicionada!')
        esc = input('Deseja adicionar mais categorias? [s/n]').lower()

def adicionar_tarefas():
    nome_cat = input('nome da categoria: ').lower()
    for categoria in categorias:
        if nome_cat == categoria[0].lower():
            escolha = 's'
            while escolha != 'n':
                tarefa = input('Digite uma tarefa: ')
                categoria[1].append(tarefa)
                escolha = input('Deseja dicionar mais tarefas? [s/n] ').lower()
            
def exibir_tarefas():
    for categoria in categorias:
        print(f'Nome da categoria: {categoria[0]}')
        print('Tarefas: ')
        cont = 1
        for tarefas in categoria[1]:
            print(f'{cont}. {tarefas}')
            cont += 1
        print()

adicionar_categoria()
adicionar_tarefas()
exibir_tarefas()