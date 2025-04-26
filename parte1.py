import parte2
categorias = []
def menu(esc):
    print('1. adicionar categoria')
    print('2. adicionar tarefa')
    print('3. ver tarefas')
    print('4. sair')
    escolha = input('Escolha uma opção: ')
    return escolha


while True:
    esc = menu(0)
    if esc == '1':
        parte2.adicionar_categorias(categorias)
    elif esc == '2':
        parte2.adicionar_tarefas(categorias)
    elif esc == '3':
        parte2.exibir_tarefas(categorias)
    elif esc == '4':
        print('Saindo')
        break
    else:
        print('Opção invalida')