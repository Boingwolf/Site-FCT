# Not yet implemented

"""
from sqlalchemy.sql.elements import Null
from utils import request,jsonify,Blueprint

bp = Blueprint('formulario', __name__)

@bp.route('/api/formulario', methods=['POST'])
def criar_formulario():
    dados = request.get_json()
    if not dados.get('nome'):
        return jsonify({"error": 'Nome é obrigatório.'}), 400
    if not dados.get('email'):
        return jsonify({"error": 'Email é obrigatório.'}), 400
    if '@' not in dados.get('email'):
        return jsonify({"error":'Email inválido'}), 400
    if not dados.get('mensagem'):
        return jsonify({'error':'Mensagem obrigatória'}), 400


    print('Dados recebidos:', dados)
    return jsonify({'mensagem': 'Formulário guardado com sucesso'}), 201

@bp.route('/api/formularios', methods=['GET'])
def listar_formularios():
    formulario=Null
    return jsonify([dict(f) for f in formularios])
"""
