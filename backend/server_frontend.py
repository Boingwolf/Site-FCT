from flask import Flask, send_from_directory
import os

app = Flask(__name__)

FRONTEND_FOLDER = os.path.join(os.path.dirname(__file__),'..', 'codigo')

@app.route('/')
def home():
    return send_from_directory(os.path.join(FRONTEND_FOLDER, 'Paginas-HTML'),'index.html')

@app.route('/Paginas-HTML/<path:filename>')
def serve_html(filename):
    return send_from_directory(
        os.path.join(FRONTEND_FOLDER, 'Paginas-HTML'),
        filename
    )

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(
        os.path.join(FRONTEND_FOLDER, 'images'),
        filename
    )

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

if __name__ == '__main__':
    print("=" * 50)
    print("🌐 Servidor Frontend do AromaWake")
    print("=" * 50)
    print(f"📂 Servindo: {FRONTEND_FOLDER}")
    print(f"🔗 Acede: http://localhost:8000")
    print("=" * 50)
    print("Pressiona Ctrl+C para parar")
    print()
    app.run(debug=True, port=8000)