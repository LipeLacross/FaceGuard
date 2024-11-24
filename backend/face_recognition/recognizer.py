import os
import face_recognition
from backend.database.models import get_user_data

KNOWN_FACES_FOLDER = os.path.join('images', 'known_faces')

def recognize_face(image_path):
    """
    Função para reconhecer o rosto de uma imagem carregada.
    """
    uploaded_image = face_recognition.load_image_file(image_path)
    uploaded_encodings = face_recognition.face_encodings(uploaded_image)

    if uploaded_encodings:
        uploaded_encoding = uploaded_encodings[0]

        for file_name in os.listdir(KNOWN_FACES_FOLDER):
            known_image_path = os.path.join(KNOWN_FACES_FOLDER, file_name)
            known_image = face_recognition.load_image_file(known_image_path)
            known_encodings = face_recognition.face_encodings(known_image)

            if known_encodings:
                known_encoding = known_encodings[0]
                match = face_recognition.compare_faces([known_encoding], uploaded_encoding)

                if match[0]:
                    user_id = file_name.split(".")[0]
                    return get_user_data(user_id)
    return None
