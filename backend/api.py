from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import formularios,contactos
import os

app = Flask(__name__)
CORS(app)

BACKEND_FOLDER = os.path.dirname(__file__)
PAGE_FODER = os.path.join(BACKEND_FOLDER,'page')

app.register_blueprint(formularios.bp)
app.register_blueprint(contactos.bp)

@app.route("/")
def home():
    return send_from_directory(
        PAGE_FODER,
        "api.html"
    )
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(PAGE_FODER, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
