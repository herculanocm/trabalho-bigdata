import pandas as pd
from persistencia.daoSqlite import BancoSqlite




# Inicia o Banco
bancoSqlite = BancoSqlite('base/exercício_final.db')


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

def receita_x_vendedor(df_pedidos, df_produtos):
    df_join = df_pedidos.join(df_produtos.set_index('id_produto'), on = 'id_produto')
    return df_join.loc[:, ['id_vendedor', 'val_produto']].groupby('id_vendedor').sum().sort_values(by='val_produto', ascending=False)

while True:
    strMenu = """ 
    Digite uma das opções abaixo do Menu: 
    1) Lista de Vendedores Disponíveis.
    2) Selecionar um Vendedor.
    3) Quantidade de Vendas x Vendedor.
    4) Quantidade de Produtos x Vendedor.
    5) Quantidade de Receita x Vendedor.
    
             
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
    elif op == 5:
        print(receita_x_vendedor(df, pd.read_sql_query("SELECT * from tb_produtos", bancoSqlite.connect())))
    else:
        print('Opção desconhecida, escolha uma opção valida.')
