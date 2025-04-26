categorias = [['casa', ['varrer', 'encher']]]
categorias[0][1].append('dormir')
print(categorias)

# def adicionar_categoria():
#     esc = 's'
#     while esc != 'n':
#         tarefas = []
#         nome_categoria = input('Nome da categoria: ')
#         if nome_categoria not in categorias:
#             escolha = 's'
#             while escolha != 'n':
#                 tarefa = input('Digite uma tarefa: ')
#                 tarefas.append(tarefa)
#                 escolha = input('Deseja dicionar mais tarefas? [s/n] ').lower()
#             categorias.append([nome_categoria, tarefas])
#             print(f'Categoria {nome_categoria} adicionada com sucesso!')
#         else:
#             print('Categoria já esta adicionada!')
#         esc = input('Deseja adicionar mais categorias? [s/n]').lower()
# adicionar_categoria()
# def exibir_tarefas():
#     for categoria in categorias:
#         print(f'Nome da categoria: {categoria[0]}')
#         print('Tarefas: ')
#         cont = 1
#         for tarefas in categoria[1]:
#             print(f'{cont}. {tarefas}')
#             cont += 1
#         print()
# exibir_tarefas()
