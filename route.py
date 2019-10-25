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
    #lista_alunos = cassio.print_all()
    #return jsonify(lista_alunos)
  

@app.route("/minhaaplicacao", methods=['POST'])
def post(): #cadastrar
    print("Todos os alunos registrados:")
    cassio.print_all()
    return "Os alunos mostrados são os que foram registrados até agora."

@app.route("/minhaaplicacao/<int:matricula>", methods=['PUT'])
def put(matricula): #??? acho que é o update aqui
    data = request.json
    cassio.update(data["nome"], data["sobrenome"], matricula)
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