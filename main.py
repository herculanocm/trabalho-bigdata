import pandas as pd
from persistencia.daoSqlite import BancoSqlite


"""
# Inicia o Banco 
bancoSqlite = BancoSqlite('base/exercício_final.db')

# Connecta o Banco 
bancoSqlite.connect()

# Realiza o comando SQL
data = bancoSqlite.execute("SELECT * FROM tb_clientes")

#Fecha a con 
bancoSqlite.close()

"""


# Inicia o Banco
bancoSqlite = BancoSqlite('base/exercício_final.db')

# Connecta o Banco
con =  bancoSqlite.connect()
cursor = con.cursor()

# Acesso a tabela de produtos
cursor.execute("""
    SELECT
        id_produto,
        nom_produto,
        cat_produto,
        val_produto
    FROM tb_produtos""")

print("{:<15}{:<20}{:<20}{:<20}".format("id_produto", "nom_produto", "cat_produto", "val_produto"))
print("–" * 95)
for linha in cursor.fetchall():
    print("{0[0]:<15}{0[1]:<20}{0[2]:<20}{0[3]:<10}".format(linha))

#df = pd.read_sql_query("SELECT * from tb_clientes", con)


# for d in list(df.values):
#     print(d)
#,names['id_cliente','id_produto','num_nf', 'dia_pedido','mês_pedido','ano_pedido','id_vendedor','qtd_vendida']


def retorna_lista_vendedores(df):
    return list(set(df['id_vendedor']))

def apurar_vendas(df, id_vendedor):
    qtd_vendas, qtd_produto = 0, 0
    dfVendas = df.loc[df.id_vendedor == id_vendedor, ['num_nf','qtd_vendida']].groupby('num_nf').sum()
    qtd_vendas = len(dfVendas)
    qtd_produto = dfVendas['qtd_vendida'].sum()
    return [id_vendedor, qtd_vendas, qtd_produto]

def vendas_x_vendedor(df):
    return df.loc[:, ['id_vendedor','num_nf']].groupby('id_vendedor').num_nf.nunique().reset_index().sort_values(by='num_nf', ascending=False)

def produtos_x_vendedor(df):
    return df.loc[:, ['id_vendedor', 'qtd_vendida']].groupby('id_vendedor').sum().sort_values(by='qtd_vendida', ascending=False)

while True:
    strMenu = """ 
    Digite uma das opções abaixo do Menu: 
    1) Lista de Vendedores Disponíveis.
    2) Selecionar um Vendedor.
    3) Quantidade de Vendas x Vendedor.
    4) Quantidade de Produtos x Vendedor.
             
    Digite 0 para sair.
    """
    op = int(input(strMenu))
    df = pd.read_csv('./base/pedidos.csv')
    if op == 0:
        break
    elif op == 1:
        print(retorna_lista_vendedores(df))
    elif op == 2:
        id_vendedor = input("Entre com o código do vendedor: ")
        lstVendas = apurar_vendas(df, id_vendedor)
        print(f'O vendedor {lstVendas[0]} totalizou {lstVendas[2]} produtos em {lstVendas[1]} vendas realizadas.')
    elif op == 3:
        print(vendas_x_vendedor(df))
    elif op == 4:
        print(produtos_x_vendedor(df))
