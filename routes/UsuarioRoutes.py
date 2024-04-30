from flask import render_template, Blueprint, request

class UsuarioRoutes():
    #Criando a instância do blueprint
    usuario_routes = Blueprint('usuario_routes', __name__,
                            template_folder='../templates/usuario_templates/')

    @usuario_routes.route('/', methods=['GET'])
    def index():
        usuario_nome = request.args.get("nome")
        return render_template('init.html', usuario = usuario_nome)


