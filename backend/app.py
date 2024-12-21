from flask import Flask, request, jsonify, send_from_directory
import os
import base64
from io import BytesIO
from PIL import Image
from backend.face_recognition.recognizer import recognize_face_with_faiss

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('backend', 'images', 'uploads')
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# Rota para servir a página inicial
@app.route('/')
def index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

# Rota para servir arquivos estáticos (CSS, JS)
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.get_json()
        if 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400

        # Processar a imagem em base64 recebida
        image_data = data['image']
        try:
            image_data = image_data.split(",")[1]
        except IndexError:
            return jsonify({"error": "Invalid image format, base64 data not found"}), 400

        # Tentar decodificar a imagem e salvar
        try:
            image = Image.open(BytesIO(base64.b64decode(image_data)))
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            image_path = os.path.join(UPLOAD_FOLDER, 'uploaded_image.png')
            image.save(image_path)
        except Exception as e:
            return jsonify({"error": f"Failed to process the image: {str(e)}"}), 500

        # Realizar reconhecimento facial usando a função do recognizer.py
        user_data = recognize_face_with_faiss(image_path)
        if user_data:
            return jsonify(user_data)
        else:
            return jsonify({"error": "No match found"}), 404

    except Exception as e:
        return jsonify({"error": f"Unexpected server error: {str(e)}"}), 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000)
