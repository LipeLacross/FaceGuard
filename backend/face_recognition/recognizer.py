import os
import face_recognition
import numpy as np
import faiss
from backend.database.models import get_user_data

# Definir o caminho da pasta onde as imagens conhecidas estão armazenadas
KNOWN_FACES_FOLDER = os.path.join('backend', 'images', 'known_faces')

# Inicializar o índice do FAISS
encoding_list = []
id_list = []

def load_known_faces():
    """
    Carrega as imagens conhecidas e seus encodings, e inicializa o índice FAISS.
    """
    global encoding_list, id_list
    for filename in os.listdir(KNOWN_FACES_FOLDER):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            known_image_path = os.path.join(KNOWN_FACES_FOLDER, filename)
            known_image = face_recognition.load_image_file(known_image_path)
            known_encoding = face_recognition.face_encodings(known_image)[0]
            encoding_list.append(known_encoding)
            user_id = filename.split(".")[0]  # Supondo que o ID do usuário está no nome do arquivo
            id_list.append(user_id)

    # Converter a lista de encodings para uma matriz NumPy
    encoding_matrix = np.array(encoding_list, dtype='float32')

    # Criar o índice FAISS e adicionar os encodings
    index = faiss.IndexFlatL2(128)  # 128 é o tamanho do vetor de encodings do face_recognition
    index.add(encoding_matrix)

    return index

# Carregar os rostos conhecidos e inicializar o índice
faiss_index = load_known_faces()

def recognize_face_with_faiss(image_path):
    """
    Função para reconhecer o rosto de uma imagem carregada usando FAISS.
    Retorna os dados do usuário se houver uma correspondência encontrada.
    """
    try:
        # Carregar a imagem de entrada e calcular o encoding
        uploaded_image = face_recognition.load_image_file(image_path)
        uploaded_encoding = face_recognition.face_encodings(uploaded_image)[0].reshape(1, -1)

        # Realizar a busca no índice FAISS
        distances, indices = faiss_index.search(uploaded_encoding.astype('float32'), 1)

        if len(indices) > 0 and distances[0][0] < 0.6:  # 0.6 é um valor de limiar para determinar uma correspondência
            user_id = id_list[indices[0][0]]
            return get_user_data(user_id)

        return None
    except Exception as e:
        print(f"Erro no reconhecimento facial com FAISS: {str(e)}")
        return None
