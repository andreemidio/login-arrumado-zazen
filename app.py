from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
import datetime


secret_key = "a4ab11c300d459c3e6d03d1320bb58ab"


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
app = Flask(__name__)

# Definindo a lista de usuarios e senhas validos
users = [
    {"username": "admin", "password": "1234"},
    {"username": "user1", "password": "abcd"},
    {"username": "user2", "password": "efgh"},
]

# Rota para exibir o formulario de login


@app.route("/login", methods=["GET"])
def login_form():
    return render_template("index.html")

# Rota para processar o login do usuario


@app.route("/login", methods=["POST"])
def login_submit():
    # Obtendo os valores do formulario de login
    input_username = request.form["username"]
    input_password = request.form["password"]

    # Verificando se o usuario e senha digitados sao validos
    for user in users:
        if input_username == user["username"] and input_password == user["password"]:
            # return "Voce foi autorizado"

            return render_template("upload.html")

        if input_username != user["username"] and input_password != user["password"]:
            return render_template("error.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    save_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(save_path)
    Nome = request.form.get("Nome")
    if Nome is None:
        print("O nome não foi enviado")

    Email = request.form.get("emaill")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('submissions.txt', 'a+') as f:
        f.write('{} - {} - {} - {}\n'.format(Nome, Email, file.filename, time))
    return render_template("upload.html")


@app.route('/get-file/<filename>')
def get_file(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + '.png')
    return send_file(file, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
