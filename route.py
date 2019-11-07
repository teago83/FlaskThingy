from flask import Flask, request, jsonify
import random
from aluno import Aluno

app = Flask(__name__)

cassio = Aluno()

@app.route("/") 
def index():
    return "Hello!"

@app.route("/minhaaplicacao", methods=['GET'])
def get(): #listar
    listis = cassio.print_all()
    print(listis)
    return jsonify(listis)

@app.route("/minhaaplicacao", methods=['POST'])
def post(): #cadastrar
    data = request.json
    matricula = 100000 + random.randint(1, 99999)
    cassio.insert(data["nome"], data["sobrenome"], matricula)
    return "Aluno(a) registrado(a) com sucesso."

@app.route("/minhaaplicacao/<int:matricula>", methods=['PUT'])
def put(matricula): #??? acho que é o update aqui
    data = request.json
    cassio.update(data["nome"], data["sobrenome"], matricula)
    return "Aluno(a) atualizado(a) com sucesso."

@app.route("/minhaaplicacao/<int:matricula>", methods=['DELETE'])
def delete(matricula): #deletar
    cassio.delete(matricula)
    return "Aluno(a) deletado(a) com sucesso."

if __name__ == '__main__':
    app.run(debug=True)