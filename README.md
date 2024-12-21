## 🌐 [English Version of README](README_EN.md)

# Sistema de Reconhecimento Facial

Este projeto é uma aplicação web que utiliza reconhecimento facial para identificar usuários com base em imagens capturadas pela câmera do dispositivo. A aplicação está dividida em duas partes principais: **Backend** (usando Flask) e **Frontend** (usando HTML, CSS e JavaScript). O sistema processa imagens em tempo real para reconhecer rostos conhecidos e fornecer informações associadas ao usuário reconhecido.

## 🔨 Funcionalidades do Projeto

- **Captura de Imagem:** Utiliza a câmera do dispositivo para capturar fotos.
- **Reconhecimento Facial:** Compara a imagem capturada com uma base de dados de rostos conhecidos.
- **Integração com Banco de Dados:** Recupera e exibe informações do usuário reconhecido a partir de um banco de dados SQLite.
- **Interface Intuitiva:** Interface amigável construída com HTML, CSS e JavaScript.
- **API Backend:** API desenvolvida em Flask para processamento e reconhecimento das imagens.

### Exemplo Visual do Projeto

![Interface do Sistema de Reconhecimento Facial](frontend/assets/screenshot.png)

*Descrição: A interface exibe a câmera em tempo real, com um botão para capturar a imagem e feedback sobre o reconhecimento.*

## ✔️ Técnicas e Tecnologias Utilizadas

- **Linguagens:**
    - Python 3.7+
    - JavaScript
    - HTML5
    - CSS3

- **Frameworks e Bibliotecas:**
    - Flask (Backend)
    - face_recognition (Reconhecimento Facial)
    - Pillow (Manipulação de Imagens)
    - Bootstrap 4.5.2 (Estilos CSS)

- **Banco de Dados:**
    - SQLite

- **Outros:**
    - Git (Controle de Versão)

## 📁 Estrutura do Projeto

```
├── README.md
├── README_EN.md
├── backend/
│   ├── app.py
│   ├── images/
│   │   └── uploads/
│   │       └── uploaded_image.png
│   ├── database/
│   │   ├── models.py
│   │   └── setup.py
│   ├── face_recognition/
│   │   └── recognizer.py
│   └── images/
│       ├── known_faces/
│       └── uploads/
├── frontend/
│   ├── app.js
│   ├── index.html
│   ├── styles.css
│   └── assets/
│       └── screenshot.png
├── ideas.txt
└── requirements.txt
```

- **backend/**
    - **app.py**: Aplicação Flask que serve a interface frontend e fornece a API para upload e reconhecimento de imagens.
    - **images/**
        - **known_faces/**: Diretório com as imagens dos rostos conhecidos.
        - **uploads/**: Diretório para armazenar as imagens carregadas.
    - **database/**
        - **models.py**: Módulo para interagir com o banco de dados SQLite.
        - **setup.py**: Script para configurar e criar o banco de dados.
    - **face_recognition/**
        - **recognizer.py**: Módulo que implementa o reconhecimento facial.
- **frontend/**
    - **index.html**: Interface do usuário para captura de imagens e interação com o backend.
    - **app.js**: Script JavaScript para capturar imagens e comunicar com o backend.
    - **styles.css**: Estilos CSS para a interface do usuário.
    - **assets/**: Diretório para armazenar arquivos estáticos, como imagens.
- **ideas.txt**: Arquivo para anotações e ideias futuras.
- **requirements.txt**: Lista de dependências Python necessárias para o backend.

## 🛠️ Abrir e Rodar o Projeto

Para iniciar o projeto localmente, siga os passos abaixo:

### 1. **Certifique-se de que o Python 3.7+ está instalado**

- Verifique a versão instalada com:

  ```bash
  python --version
  ```

- Se não estiver instalado, baixe e instale a versão recomendada do [Python](https://www.python.org/downloads/).

### 2. **Clone o Repositório**

- Copie a URL do repositório e execute o comando abaixo no terminal:

  ```bash
  git clone <URL_DO_REPOSITORIO>
  ```

### 3. **Configuração do Backend**

#### a. **Crie e Ative um Ambiente Virtual**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

#### b. **Instale as Dependências**

```bash
pip install -r ../requirements.txt
```

**Conteúdo sugerido para `requirements.txt`:**

```plaintext
Flask==2.0.3
face_recognition==1.3.0
Pillow==9.0.1
gunicorn==20.1.0
```

#### c. **Configuração do Banco de Dados**

Execute o script de configuração para criar o banco de dados SQLite.

```bash
python database/setup.py
```

#### d. **Adicionar Usuários Conhecidos**

1. **Inserir Dados no Banco de Dados:**

   Utilize um cliente SQLite ou script Python para inserir usuários na tabela `users`. Cada usuário deve ter um `id`, `name`, `address` e `photo_path`.

   **Exemplo de Inserção via Script Python:**

   ```python
   import sqlite3

   DATABASE = 'backend/database/users.db'

   def add_user(user_id, name, address, photo_path):
       with sqlite3.connect(DATABASE) as conn:
           cursor = conn.cursor()
           cursor.execute("INSERT INTO users (id, name, address, photo_path) VALUES (?, ?, ?, ?)",
                          (user_id, name, address, photo_path))
           conn.commit()

   if __name__ == "__main__":
       add_user(1, "João Silva", "Rua Exemplo, 123", "backend/images/known_faces/1.jpg")
       # Adicione mais usuários conforme necessário
       print("Usuários adicionados com sucesso!")
   ```

2. **Adicionar Imagens Conhecidas:**

   Coloque as imagens dos usuários na pasta `backend/images/known_faces/`. O nome do arquivo deve corresponder ao `user_id` do usuário (e.g., `1.jpg` para `user_id=1`).

### 4. **Executando o Backend**

Certifique-se de estar no ambiente virtual e execute a aplicação Flask.

```bash
python app.py
```

A aplicação estará acessível em `http://0.0.0.0:5000/`.

### 5. **Configuração do Frontend**

O frontend está contido na pasta `frontend/` e consiste em arquivos estáticos que são servidos pelo Flask.

#### a. **Acessando a Aplicação**

Abra um navegador e vá para `http://localhost:5000/`. A página inicial exibirá a interface de captura de imagem.

#### b. **Permissões da Câmera**

Certifique-se de que o navegador tem permissão para acessar a câmera do dispositivo. Se solicitado, permita o acesso.

## 🌐 Deploy

Para fazer o deploy da aplicação, siga os passos básicos abaixo:

1. **Escolha uma Plataforma de Hosting**
    - **Heroku:** Plataforma como serviço que suporta aplicações Flask.
    - **AWS Elastic Beanstalk:** Serviço da Amazon para deploy de aplicações web.
    - **DigitalOcean:** VPS para hospedar a aplicação.

2. **Configuração Básica para Produção**
    - Utilize um servidor web como Gunicorn.
    - Configure variáveis de ambiente necessárias.
    - Garanta que o banco de dados esteja configurado para produção.
