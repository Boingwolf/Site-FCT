from utils import request,jsonify,Blueprint
from database import get_db_connection

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
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO formularios (nome,email,telefone, mensagem)
                   VALUES (?,?,?,?)
        ''',(dados.get('nome'),dados.get('email'),dados.get('telefone', ''),dados.get('mensagem')))
    conn.commit()
    conn.close()
    print('Dados recebidos:', dados)
    return jsonify({'mensagem': 'Formulário guardado com sucesso'}), 201

@bp.route('/api/formularios', methods=['GET'])
def listar_formularios():
    conn = get_db_connection()
    formularios = conn.execute('SELECT * FROM formularios ORDER BY data_criacao DESC').fetchall()
    conn.close()
    return jsonify([dict(f) for f in formularios])