from db.models import Contacto
from db.session import session

from utils import Blueprint, jsonify, request

bp = Blueprint("contacto", __name__)
sessao = session


@bp.route("/api/contacto", methods=["POST"])
def criar_contacto():
    dados: dict = request.get_json()
    if not dados.get("nome"):
        return jsonify({"error": "Nome é obrigatório."}), 400
    if not dados.get("email"):
        return jsonify({"error": "Email é obrigatório."}), 400
    if "@" not in str(dados.get("email")):
        return jsonify({"error": "Email inválido"}), 400
    if not dados.get("mensagem"):
        return jsonify({"error": "Mensagem obrigatória"}), 400
    contactoNovo: Contacto = Contacto(
        nome=dados.get("nome"), email=dados.get("email"), mensagem=dados.get("mensagem")
    )
    sessao.add(contactoNovo)
    sessao.commit()
    print("Dados recebidos:", dados)
    return jsonify({"mensagem": "Contacto guardado com sucesso"}), 201


@bp.route("/api/contactos", methods=["GET"])
def listar_contactos():
    contactosRaw: list = sessao.query(Contacto).all()
    contactos: dict = {}
    print("Contactos:", contactosRaw)
    for contacto in contactosRaw:
        print(contacto.nome, contacto.email, contacto.mensagem)
        contactos[contacto.id] = {
            "nome": contacto.nome,
            "email": contacto.email,
            "mensagem": contacto.mensagem,
        }
    return jsonify(contactos)
