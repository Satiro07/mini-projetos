lista = [['jose', 5, 7, 9], ['wagner', 6, 8, 8]]
lista_nova = []
def list_dict(lista_dicionario):
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
        return lista_nova
    except ValueError:
        print('Nao condiz com o esperado')

print(list_dict(lista))