import psycopg2
from connection import Connection

class Aluno():

    def insert(self, nome, sobrenome, matricula):
        try:
            conexao = Connection()
            conexao.insert("insert into aluno (nome, sobrenome, matricula) values ('{0}', '{1}', '{2}')".format(nome, sobrenome, matricula))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        
    def delete(self, matricula):
        try:
            conexao = Connection()
            conexao.delete("delete from aluno where matricula = {0}".format(matricula))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        
    def print_all(self):
        try:
            conexao = Connection()
            result = conexao.print_all('select * from aluno')
            for i in result:
                print("Nome = ", i[0])
                print("Sobrenome = ", i[1])
                print("Matrícula = ", i[2], "\n")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

    def print_one(self, matricula):
        try:
            conexao = Connection()
            result = conexao.print_one('select * from aluno where matricula = {0}'.format(matricula))
            print("Nome = ", result[0][0])
            print("Sobrenome = ", result[0][1])
            print("Matrícula = ", result[0][2])
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

    def update(self, nome, sobrenome, matricula):
        try:
            conexao = Connection()
            conexao.update("update aluno set nome = {0}, sobrenome = {1} where matricula = {2}".format(nome, sobrenome, matricula))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
