listas = ['jose', 5, 7, 9]
# lista = []
lista_nova = []
def list_dict(lista_dicionario):
    lista_geral = lista_dicionario
    def menu_verificacoes():
        print('1. somente uma lista')
        print('2. sublistas')
        print('3. dicionario com listas')

    def all_verificacoes(lista):
        lista_dicionario = lista
        def verificacao_lista(lista_dicionario):
            try:
                lista_temp = []
                for item in lista_dicionario:
                    if str(item) == item:
                        lista_nova.append(item)
                    elif float(item) == item or int(int) == item:
                        lista_temp.append(float(item))
                    else:
                        pass
                lista_nova.append(lista_temp)
                return lista_nova, '1'
            except ValueError:
               return '0', '0'
        rep = verificacao_lista(lista)
        if rep == '1':
            return rep[1]
    resp = all_verificacoes(lista_geral)
    if resp == '1':
        return lista_nova

print(list_dict(listas))