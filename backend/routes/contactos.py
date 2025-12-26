from utils import request,jsonify,Blueprint
from database import get_db_connection

bp = Blueprint('contacto', __name__)

@bp.route('/api/contacto', methods=['POST'])
def criar_contacto():
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
        INSERT INTO contactos (nome,email,assunto, mensagem)
                   VALUES (?,?,?,?)
        ''',(dados.get('nome'),dados.get('email'),dados.get('assunto', ''),dados.get('mensagem')))
    conn.commit()
    conn.close()
    print('Dados recebidos:', dados)
    return jsonify({'mensagem': 'Contacto guardado com sucesso'}), 201

@bp.route('/api/contactos', methods=['GET'])
def listar_contactos():
    conn = get_db_connection()
    contactos = conn.execute('SELECT * FROM contactos ORDER BY data_criacao DESC').fetchall()
    conn.close()
    return jsonify([dict(c) for c in contactos])
