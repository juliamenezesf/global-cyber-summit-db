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
        return jsonify({"mensagem": f"Erro: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)