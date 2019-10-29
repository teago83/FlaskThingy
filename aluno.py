import psycopg2
from connection import Connection
from flask import jsonify

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
            lista_alunos = []
            for i in result:
                dict_aluno = {"Nome" : i[0], "Sobrenome": i[1], "Matrícula": i[2]}
                lista_alunos.append(dict_aluno)
            return lista_alunos
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        

    def print_one(self, matricula):
        try:
            conexao = Connection()
            result = conexao.print_one('select * from aluno where matricula = {0}'.format(matricula))
            return jsonify(nome=result[0][0],
                           sobrenome=result[0][1],
                           matricula=result[0][2])
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

    def update(self, nome, sobrenome, matricula):
        try:
            conexao = Connection()
            conexao.update("update aluno set nome = '{0}', sobrenome = '{1}' where matricula = {2}".format(nome, sobrenome, matricula))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
