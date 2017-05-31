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

#df = pd.read_sql_query("SELECT * from tb_clientes", con)


# for d in list(df.values):
#     print(d)
#,names['id_cliente','id_produto','num_nf', 'dia_pedido','mês_pedido','ano_pedido','id_vendedor','qtd_vendida']


def retorna_lista_vendedores(df):
    return list(set(df['id_vendedor']))


while True:
    op = int(input("Digite uma das opções abaixo do Menu : \n 1) Lista de Vendedores Disponiveis. \n Digite 0 para sair. \n "))
    df = pd.read_csv('./base/pedidos.csv')
    if op == 0:
        break
    elif op == 1:
        print(retorna_lista_vendedores(df))


#TESTE DE COMMIT