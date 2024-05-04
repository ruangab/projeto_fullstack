from flask import render_template, Blueprint, request, jsonify
from models.Database import Database

class UsuarioRoutes():
    #Criando a instância do blueprint
    usuario_routes = Blueprint('usuario_routes', __name__,
                            template_folder='../templates/usuario_templates/')

    @usuario_routes.route('/', methods=['GET'])
    def index():
        usuario_nome = request.args.get("nome")
        return render_template('init.html', usuario = usuario_nome)

    @usuario_routes.route("/cadastro", methods = ["POST"])
    def cadastro():
        email_usuario = request.form["email_usuario"]
        senha_usuario = request.form["senha_usuario"]

        usuario_banco = Database._insert_one(
            {
                "email_usuario":email_usuario,
                "senha_usuario":senha_usuario,
            },
            collection_name="usuarios"
        ) 

        return jsonify({
            "status":"sucesso",
            "mensagem":"Usuário cadastrado"
        })


    @usuario_routes.route("/login", methods = ["POST"])
    def login():
        email_usuario = request.form["email_usuario"]
        senha_usuario = request.form["senha_usuario"]

        usuario_banco = Database._find_one(
            {
                "email_usuario":email_usuario,
                "senha_usuario":senha_usuario,
            },
            collection_name="usuarios"
        )

        if usuario_banco is None:
            return jsonify({
                "status":"erro",
                "mensagem":"Usuario não cadastrado"
            })
    
        return jsonify({
            "status":"sucesso",
            "data":{
                "email_usuario":usuario_banco["email_usuario"]
            },
            "mensagem":"Usuário logado com sucesso"
        })
    
    @usuario_routes.route("/delete", methods = ["DELETE"])
    def delete():
        email_usuario = request.form["email_usuario"]
        senha_usuario = request.form["senha_usuario"]

        usuario_banco = Database._delete_one(
            {
                "email_usuario":email_usuario,
                "senha_usuario":senha_usuario,
            },
            collection_name="usuarios"
        )

        if usuario_banco is None:
            return jsonify({
                "status":"erro",
                "mensgem":"Erro ao deletar"
            })
        
        if usuario_banco.deleted_count == 0:
            return jsonify({
                "status":"erro",
                "mensgem":"Usuário não cadastrado"
            })
    
        return jsonify({
            "status":"sucesso",
            "mensagem":"Usuario deletado!"
        })
    
    @usuario_routes.route("/editar", methods = ["PUT"])
    def put():
        email_usuario = request.form["email_usuario"]
        senha_usuario_antiga = request.form["senha_usuario_antiga"]
        senha_usuario_nova = request.form["senha_usuario_nova"]

        usuario_banco = Database._update_one(
            query={
                "email_usuario":email_usuario,
                "senha_usuario":senha_usuario_antiga
            },
            document = {
                "email_usuario":email_usuario,
                "senha_usuario":senha_usuario_nova
            },
            collection_name="usuarios"
        )

        if usuario_banco is None:
            return jsonify({
                "status":"erro",
                "mensgem":"Erro ao atualizar"
            })
        
        if usuario_banco.modified_count == 0:
            return jsonify({
                "status":"erro",
                "mensgem":"Usuário não atualizado"
            })
    
        return jsonify({
            "status":"sucesso",
            "mensagem":"Usuario Atualizado!"
        })

    @usuario_routes.route("/usuarios", methods = ["POST"])
    def usuarios():
        usuario_banco = Database._find_all(
            query={},
            collection_name="usuarios"
        )

        if usuario_banco is None:
            return jsonify({
                "status":"erro",
                "mensgem":"Erro ao atualizar"
            })
    
        usuarios_tradados = list(map(
            lambda x: {
                "email_usuario":x["email_usuario"]
            },
            usuario_banco
        ))   

        return jsonify({
            "status":"sucesso",
            "data":usuarios_tradados,
            "mensagem":"Usuario Atualizado!"
        })


