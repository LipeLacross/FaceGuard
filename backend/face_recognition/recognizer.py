import os
import face_recognition
from backend.database.models import get_user_data

# Definir o caminho da pasta onde as imagens conhecidas estão armazenadas
KNOWN_FACES_FOLDER = os.path.join('backend', 'images', 'known_faces')

def recognize_face(image_path):
    """
    Função para reconhecer o rosto de uma imagem carregada usando face_recognition.
    Retorna os dados do usuário se houver uma correspondência encontrada.
    """
    try:
        uploaded_image = face_recognition.load_image_file(image_path)
        uploaded_encoding = face_recognition.face_encodings(uploaded_image)[0]

        for filename in os.listdir(KNOWN_FACES_FOLDER):
            known_image_path = os.path.join(KNOWN_FACES_FOLDER, filename)
            known_image = face_recognition.load_image_file(known_image_path)
            known_encoding = face_recognition.face_encodings(known_image)[0]

            match = face_recognition.compare_faces([known_encoding], uploaded_encoding)
            if match[0]:
                user_id = filename.split(".")[0]  # Supondo que o ID do usuário está no nome do arquivo
                return get_user_data(user_id)
        return None
    except Exception:
        return None
