from flask import Flask, send_from_directory
import os

app = Flask(__name__)

CODIGO_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'codigo')

@app.route('/')
def home():
    return send_from_directory(
        os.path.join(CODIGO_FOLDER, 'Paginas-HTML'),
        'index.html'
    )
@app.route('/<path:filename>')
def serve_file(filename):
    # Tenta na raiz primeiro
    filepath = os.path.join(CODIGO_FOLDER, filename)
    if os.path.isfile(filepath):
        return send_from_directory(CODIGO_FOLDER, filename)
    
    filepath = os.path.join(CODIGO_FOLDER, 'Paginas-HTML', filename)
    if os.path.isfile(filepath):
        return send_from_directory(
            os.path.join(CODIGO_FOLDER, 'Paginas-HTML'),
            filename
        )
    
    filepath = os.path.join(CODIGO_FOLDER, 'images', filename)
    if os.path.isfile(filepath):
        return send_from_directory(
            os.path.join(CODIGO_FOLDER, 'images'),
            filename
        )
    return "Ficheiro não encontrado", 404

if __name__ == '__main__':
    print("=" * 50)
    print("🌐 Servidor Frontend do AromaWake")
    print("=" * 50)
    print(f"📂 Servindo: {CODIGO_FOLDER}")
    print(f"🔗 Acede: http://localhost:8000")
    print(f"🔗 API Backend: http://localhost:5000")
    print("=" * 50)
    print("Pressiona Ctrl+C para parar")
    print()
    app.run(debug=True, port=8000)