categorias = [['casa', []]]
def adicionar_categoria():
    esc = 's'
    while esc != 'n':
        nome_escolha_categoriaegoria = input('Nome da categoria: ')
        if nome_escolha_categoriaegoria not in categorias:
            categorias.append([nome_escolha_categoriaegoria, []])
            print(f'Categoria {nome_escolha_categoriaegoria} adicionada com sucesso!')
        else:
            print('Categoria já esta adicionada!')
        esc = input('Deseja adicionar mais categorias? [s/n]').lower()

def adicionar_tarefas():
    if not categorias:
        print('Nenhuma categoria adicionada! Você precisa adicionar pelo menos uma!')
    else:
        for categoria in categorias:
            print(f'Nome da categoria: {categoria[0]}')

        nome_escolha_categoria = input('Nome da categoria que deseja adicionar : ').lower()
        for categoria in categorias:
            if nome_escolha_categoria == categoria[0].lower():
                escolha = 's'
                while escolha != 'n':
                    tarefa = input('Digite uma tarefa: ')
                    categoria[1].append(tarefa)
                    escolha = input('Deseja adicionar mais tarefas? [s/n] ').lower()
            
def exibir_tarefas():
    verificacao = False
    if not categorias:
        print('Nenhuma categoria adicionada! Você precisa adicionar pelo menos uma!')
    else: 
        for categoria in categorias:
            if categoria[1] != []:
                verificacao = True
                print(f'Nome da categoria: {categoria[0]}')
                print('Tarefas: ')
                cont = 1
                for tarefas in categoria[1]:
                    print(f'{cont}. {tarefas}')
                    cont += 1
                print()
    if verificacao == False:
        print('Nenhuma tarefa adicionada!')

esco = 3
if esco == 1:
    adicionar_categoria()
elif esco == 2: 
    adicionar_tarefas()
elif esco == 3:
    exibir_tarefas()