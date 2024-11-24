from flask import Flask, request, jsonify
import os
import base64
from io import BytesIO
from PIL import Image
import face_recognition
from face_recognition.recognizer import recognize_face

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('images', 'uploads')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    image_data = data['image']
    image_data = image_data.split(",")[1]

    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image_path = os.path.join(UPLOAD_FOLDER, 'uploaded_image.png')
    image.save(image_path)

    user_data = recognize_face(image_path)
    if user_data:
        return jsonify(user_data)

    return jsonify({"error": "No match found"})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000)
