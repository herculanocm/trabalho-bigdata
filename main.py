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

df = pd.read_sql_query("SELECT * from tb_clientes", con)


for d in list(df.values):
    print(d)
