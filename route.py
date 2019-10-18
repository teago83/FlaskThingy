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
    predo = {
        "nome" : nome,
        "sobrenome" : sobrenome,
        "matrícula" : matricula,
    }
    return predo

@app.route("/minhaaplicacao", methods=['POST'])
def post(): #mostrar
    return "batata"

@app.route("/minhaaplicacao/<int:id>", methods=['PUT'])
def put(id): #???
    pass

@app.route("/minhaaplicacao/<int:id>", methods=['DELETE'])
def delete(id): #deletar
    print(id)


if __name__ == '__main__':
    app.run(debug=True)