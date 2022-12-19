from flask import Flask, request, render_template

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
            return "Voce foi autorizado"

    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
