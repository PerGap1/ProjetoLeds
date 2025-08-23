from flask import Flask, render_template, request
from Logica import Core

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.form["escolha"] and request.form["identificador"]:
        escolha = int(request.form["escolha"])
        identificador = request.form["identificador"]

        listaDados, objeto = Core.core(escolha, identificador)

        if escolha == 1:
            return render_template("Home.html", concursos=listaDados, candidato=objeto)
        elif escolha == 2:
            return render_template("Home.html", candidatos=listaDados, concurso=objeto)
        return "<h1>Erro</h1>"
    
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True) #Tirar o debug depois