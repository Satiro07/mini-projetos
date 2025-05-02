import psycopg2

conexao = psycopg2.connect(
    dbname = "aguas_test",
    user = "postgres",
    password = "162403",
    host = "localhost"
)

executar = conexao.cursor()

executar.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(50)
);
""")

executar.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES clientes(id_cliente),
    valor_pedido NUMERIC(10,2),
    data_pedido DATE,
    descricao TEXT
);
""")

conexao.commit()

def menu(ent):
    print('Opções:')
    print('1. adicionar cliente')
    print('2. adicionar valor do pedido')
    print('3. listar clientes')
    print('4. atualizar valor do pedido/data/descrição')
    print('5. Zerar valor pedido, data e descrição automaticamente')
    print('6. sair')
    escolha = input('Escolha uma opção: ')
    return escolha

def adicionar_cliente():
    nome_cliente = input('Nome do cliente: ')
    executar.execute("INSERT INTO clientes (nome_cliente) VALUES (%s)", (nome_cliente,))
    conexao.commit()
    

def add_valor_pedido():
    executar.execute("SELECT * FROM clientes")
    clientes = executar.fetchall()
    for cliente in clientes:
        print(f'ID: {cliente[0]}, Nome: {cliente[1]}')
    id_cliente = int(input('ID do cliente no qual você deseja adicionar valor: '))
    valor_pedido = float(input('Valor do pedido R$'))
    data_pedido = input('Data do pedido (Formato: YYYY-MM-DD): ')
    descricao = input('Descrição do pedido: ')
    executar.execute("INSERT INTO pedidos (id_cliente, valor_pedido, data_pedido, descricao) VALUES (%s, %s, %s, %s)", (id_cliente, valor_pedido, data_pedido, descricao))
    conexao.commit()

def listar_clientes():
    executar.execute('SELECT c.nome_cliente AS "Nome do cliente", p.valor_pedido AS "Valor do pedido", p.data_pedido AS "Data do pedido", p.descricao AS "Descrição do pedido" FROM pedidos p INNER JOIN clientes c ON p.id_cliente = c.id_cliente')
    clientes_pedidos = executar.fetchall()
    print()
    print('Clientes cadastrados')
    print()
    for cliente in clientes_pedidos:
        print(f'Nome do cliente: {cliente[0]}')
        print(f'Valor do pedido: R${cliente[1]}, Data do pedido: {cliente[2]}')
        print(f'Descrição do pedido: {cliente[3]}')
        print()
        print('_'*50)
        print()

def atualizar_valor():
    editar = input('O que deseja editar? [valor = 1, data = 2, descricao = 3] ')
    print()
    print('Clientes cadastrados')
    print()
    if editar == '1':
        executar.execute('SELECT p.id_pedido AS "ID do pedido", c.nome_cliente AS "Nome do cliente", p.valor_pedido AS "Valor do pedido" FROM pedidos p INNER JOIN clientes c ON p.id_cliente = c.id_cliente')
        clientes_pedidos = executar.fetchall()
        for cliente in clientes_pedidos:
            print(f'ID do pedido: {cliente[0]}')
            print(f'Nome do cliente: {cliente[1]}') 
            print(f'Valor do pedido: R${cliente[2]:.2f}')
            print()
            print('_'*50)
            print()

        id_pedido = int(input('ID do cliente que deseja mudar o valor: '))
        novo_valor = float(input('R$'))
        executar.execute("UPDATE pedidos SET valor_pedido = (%s) WHERE id_pedido = (%s);", (novo_valor, id_pedido))
        conexao.commit()
    elif editar == '2':
        executar.execute('SELECT p.id_pedido AS "ID do pedido", c.nome_cliente AS "Nome do cliente", p.valor_pedido AS "Valor do pedido", p.data_pedido AS "Data do pedido" FROM pedidos p INNER JOIN clientes c ON p.id_cliente = c.id_cliente')
        clientes_pedidos = executar.fetchall()
        for cliente in clientes_pedidos:
            print(f'ID pedido: {cliente[0]}')
            print(f'Nome do cliente: {cliente[1]}')
            print(f'Valor do pedido: R${cliente[2]}, Data do pedido: {cliente[3]}')
            print()
            print('_'*50)
            print()
        id_pedido = int(input('ID do pedido que deseja mudar o valor: '))
        nova_data = input('Data atualizada do pedido (Formato: YYYY-MM-DD): ')
        executar.execute("UPDATE pedidos SET data_pedido = (%s) WHERE id_pedido = (%s);", (nova_data, id_pedido))
        conexao.commit()
    elif editar == '3':
        executar.execute('SELECT p.id_pedido AS "ID do pedido", c.nome_cliente AS "Nome do cliente", p.valor_pedido AS "Valor do pedido", p.data_pedido AS "Data do pedido", p.descricao FROM pedidos p INNER JOIN clientes c ON p.id_cliente = c.id_cliente')
        clientes_pedidos = executar.fetchall()
        for cliente in clientes_pedidos:
            print(f'ID pedido: {cliente[0]}')
            print(f'Nome do cliente: {cliente[1]}') 
            print(f'Valor do pedido: R${cliente[2]}, Data do pedido: {cliente[3]}')
            print(f'Descrição: {cliente[4]}')
            print()
            print('_'*50)
            print()

        id_pedido = int(input('ID do pedido que deseja mudar o valor: '))
        nova_descricao = input('Descrição atualizada do pedido: ')
        executar.execute("UPDATE pedidos SET descricao = (%s) WHERE id_pedido = (%s);", (nova_descricao, id_pedido))
        conexao.commit()

def zerar_pedido_automaticamente():
    executar.execute('SELECT p.id_pedido AS "ID do pedido", c.nome_cliente AS "Nome do cliente", p.valor_pedido AS "Valor do pedido", p.data_pedido AS "Data do pedido" FROM pedidos p INNER JOIN clientes c ON p.id_cliente = c.id_cliente')
    clientes_pedidos = executar.fetchall()
    for cliente in clientes_pedidos:
        print(f'ID pedido: {cliente[0]}')
        print(f'Nome do cliente: {cliente[1]}')
        print(f'Valor do pedido: R${cliente[2]}, Data do pedido: {cliente[3]}')
        print()
        print('_'*50)
        print()
    id_pedido = int(input('ID do pedido que deseja mudar o valor: '))
    nova_data = '0001-01-01'
    novo_valor = 0.00
    nova_descricao = 'Está devendo nada'
    executar.execute("UPDATE pedidos SET data_pedido = (%s) WHERE id_pedido = (%s);", (nova_data, id_pedido))
    conexao.commit()
    executar.execute("UPDATE pedidos SET valor_pedido = (%s) WHERE id_pedido = (%s);", (novo_valor, id_pedido))
    conexao.commit()
    executar.execute("UPDATE pedidos SET descricao = (%s) WHERE id_pedido = (%s);", (nova_descricao, id_pedido))
    conexao.commit()



while True:
    resp = menu(0)
    if resp == '1':
        adicionar_cliente()
    elif resp == '2':
        add_valor_pedido()
    elif resp == '3':
        listar_clientes()
    elif resp == '4':
        atualizar_valor()
    elif resp == '5':
        zerar_pedido_automaticamente()
    elif resp == '6':
        print('Fim do programa')
        conexao.close()
        break
    else:
        print('Opção inválida!')
