from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

@app.route("/minhaaplicacao", methods=['GET'])
def get():
    return "teste"

@app.route("/minhaaplicacao", methods=['POST'])
def post():
    data = request.json

    return jsonify(data)

@app.route("/minhaaplicacao/<int:id>", methods=['PUT'])
def put(id):
    pass

@app.route("/minhaaplicacao/<int:id>", methods=['DELETE'])
def delete(id):
    print(id)


if __name__ == '__main__':
    app.run(debug=True)