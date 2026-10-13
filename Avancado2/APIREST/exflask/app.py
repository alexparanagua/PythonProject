from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def raiz():
    return jsonify({"mensagem": "API no ar!"})

# pip install flask
# flask --app app_flask run