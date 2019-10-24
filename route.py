from flask import Flask, request, jsonify
import random
from aluno import Aluno

app = Flask(__name__)

cassio = Aluno()

@app.route("/") 
def index():
    return "Hello!"

@app.route("/minhaaplicacao", methods=['GET'])
def get(): #cadastrar
    print("Cadastro do(a) aluno(a):")
    nome = input("Digite o nome do(a) aluno(a):")
    sobrenome = input("Digite o sobrenome do(a) aluno(a):")
    matricula = 100000 + random.randint(1, 99999)
    print("Matrícula atribuída: %d" % (matricula))
    cassio.insert(nome, sobrenome, matricula)
    return "Aluno(a) matriculado(a) com sucesso."

@app.route("/minhaaplicacao", methods=['POST'])
def post(): #mostrar
    print("Todos os alunos registrados:")
    cassio.print_all()
    return "Os alunos mostrados são os que foram registrados até agora."

@app.route("/minhaaplicacao", methods=['PUT'])
def put(): #??? acho que é o update aqui
    print("Atualizar dados de um(a) aluno(a):")
    matricula = int(input("Digite a matrícula do(a) aluno(a) que terá seus dados atualizados:"))
    nome = input("Digite o novo nome do(a) aluno(a):")
    sobrenome = input("Digite o novo sobrenome do(a) %s:" % (nome))
    cassio.update(matricula, nome, sobrenome)
    return "Aluno(a) atualizado(a) com sucesso."

@app.route("/minhaaplicacao", methods=['DELETE'])
def delete(): #deletar
    print("Deletar dados de um(a) aluno(a):")
    matricula = int(input("Digite a matrícula do(a) aluno(a)"
                          "que terá seus dados deletados:"))
    cassio.delete(matricula)
    return "Aluno(a) deletado(a) com sucesso."

if __name__ == '__main__':
    app.run(debug=True)