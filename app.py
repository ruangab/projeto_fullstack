from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return {"msg":"Ola mundo"}

@app.route("/mensagem", methods=["GET"])
def rend_template():
    h1 = request.args.get("h1")
    h2 = request.args.get("h2")

    return render_template("template_1.html", texto={
        "h1":h1,
        "h2":h2
    })
    
@app.route("/login", methods=["GET"])
def login():
    return render_template("usuario_templates/usuario-login.html")


#Importação da classe onde fica o blueprint
from routes.UsuarioRoutes import UsuarioRoutes
#Adicionando o blueprint na instância principal do flask
app.register_blueprint(UsuarioRoutes.usuario_routes, url_prefix = "/usuario")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=19980, debug=True)