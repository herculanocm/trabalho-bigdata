import sqlite3

class BancoSqlite(object):

    """Inicializacao do Banco"""
    def __init__(self, database='exercício_final.db'):
        # Nome do Banco
        self.database = database


    def connect(self):
        """Conectando ao SQLite3 database."""

        self.connection = sqlite3.connect(self.database)
        self.connected = True
        return self.connection

    def close(self):
        """Fechando a conexao """

        self.connection.commit()
        self.connection.close()
        self.connected = False

    def execute(self, statement):
        if not self.connected:
            self.connect()
        queries = []
        self.cursor = self.connection.cursor()
        self.cursor.execute(statement.strip())
        data = self.cursor.fetchall()
        """queries.append(data)"""
        return data