from flask import Flask, jsonify
from flask_cors import CORS
from varredura import executar_varredura

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return "API rodando!"

@app.route('/processar', methods=['POST'])
def processar():
    try:
        executar_varredura()
        return jsonify({"mensagem": "Varredura executada com sucesso!"})
    except Exception as e:
        return jsonify({"mensagem": f"Erro: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)