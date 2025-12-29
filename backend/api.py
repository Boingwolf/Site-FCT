from flask import Flask
from flask_cors import CORS
from routes import formularios,contactos
from database import init_db

app = Flask(__name__)
CORS(app)

init_db()

app.register_blueprint(formularios.bp)
app.register_blueprint(contactos.bp)

@app.route("/")
def home():
    return "Aromawake Backend stay be working"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
