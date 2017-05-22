from persistencia.daoSqlite import BancoSqlite

""" Inicia o Banco """
bancoSqlite = BancoSqlite('base/exercício_final.db')

""" Connecta o Banco """
bancoSqlite.connect()

""" Realiza o comando SQL """
data = bancoSqlite.execute("SELECT * FROM tb_clientes")

""" Fecha a con """
bancoSqlite.close()

for d in data:
    print(d)
