import psycopg2

class Connection():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                password="ads",
                host="127.0.0.1",
                port="5432",
                database="banco_aluno")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Ocorreu uma falha na conexão.")

    def insert(self, query):
        try:
            self.cursor.execute(query)
        except:
            print("Houve uma falha na inserção.")

    def delete(self, query):
        try:
            self.cursor.execute(query)
        except:
            print("Aconteceu um erro ao deletar.")
    
    def print_all(self, query):
        try:
            result = self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except:
            print("O processo de mostrar tudo resultou em uma falha.")

    def print_one(self, query):
        try:
            result = self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except:
            print("Não foi possível completar o processo devido a um erro.")

    def update(self, query):
        try:
            self.cursor.execute(query)
        except:
            print("Um erro impossibilitou a atualização.")
