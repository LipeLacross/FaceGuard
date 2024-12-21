## 🌐 [English Version of README](README_EN.md)

# Facial Recognition System

This project is a web application that utilizes facial recognition to identify users based on images captured by the device's camera. The application is divided into two main parts: **Backend** (using Flask) and **Frontend** (using HTML, CSS, and JavaScript). The system processes real-time images to recognize known faces and provide associated information about the recognized user.

## 🔨 Project Features

- **Image Capture:** Utilizes the device's camera to capture photos.
- **Facial Recognition:** Compares the captured image with a database of known faces.
- **Database Integration:** Retrieves and displays recognized user information from a SQLite database.
- **Intuitive Interface:** User-friendly interface built with HTML, CSS, and JavaScript.
- **Backend API:** Flask-based API for processing and recognizing images.

### Visual Example of the Project

![Facial Recognition System Interface](frontend/assets/screenshot.png)

*Description: The interface displays the live camera feed with a button to capture the image and feedback on the recognition process.*

## ✔️ Technologies and Tools Used

- **Languages:**
    - Python 3.7+
    - JavaScript
    - HTML5
    - CSS3

- **Frameworks and Libraries:**
    - Flask (Backend)
    - face_recognition (Facial Recognition)
    - Pillow (Image Processing)
    - Bootstrap 4.5.2 (CSS Styling)

- **Database:**
    - SQLite

- **Others:**
    - Git (Version Control)

## 📁 Project Structure

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
    - **app.py**: Flask application that serves the frontend interface and provides the API for image upload and recognition.
    - **images/**
        - **known_faces/**: Directory containing images of known faces.
        - **uploads/**: Directory for storing uploaded images.
    - **database/**
        - **models.py**: Module for interacting with the SQLite database.
        - **setup.py**: Script to set up and create the database.
    - **face_recognition/**
        - **recognizer.py**: Module implementing facial recognition functionality.
- **frontend/**
    - **index.html**: User interface for capturing images and interacting with the backend.
    - **app.js**: JavaScript script for capturing images and communicating with the backend.
    - **styles.css**: CSS styles for the user interface.
    - **assets/**: Directory for storing static files, such as images.
- **ideas.txt**: File for notes and future ideas.
- **requirements.txt**: List of Python dependencies required for the backend.

## 🛠️ Running the Project

To run the project locally, follow the steps below:

### 1. **Ensure Python 3.7+ is Installed**

- Verify the installed version with:

  ```bash
  python --version
  ```

- If not installed, download and install the recommended version from the [Python website](https://www.python.org/downloads/).

### 2. **Clone the Repository**

- Copy the repository URL and execute the following command in the terminal:

  ```bash
  git clone <REPOSITORY_URL>
  ```

### 3. **Backend Setup**

#### a. **Create and Activate a Virtual Environment**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### b. **Install Dependencies**

```bash
pip install -r ../requirements.txt
```

**Suggested `requirements.txt` Content:**

```plaintext
Flask==2.0.3
face_recognition==1.3.0
Pillow==9.0.1
gunicorn==20.1.0
```

#### c. **Database Setup**

Run the setup script to create the SQLite database.

```bash
python database/setup.py
```

#### d. **Add Known Users**

1. **Insert Data into the Database:**

   Use a SQLite client or a Python script to add users to the `users` table. Each user should have an `id`, `name`, `address`, and `photo_path`.

   **Example Insertion via Python Script:**

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
       add_user(1, "John Doe", "123 Example Street", "backend/images/known_faces/1.jpg")
       # Add more users as needed
       print("Users added successfully!")
   ```

2. **Add Known Images:**

   Place the users' images in the `backend/images/known_faces/` folder. The filename should correspond to the `user_id` (e.g., `1.jpg` for `user_id=1`).

### 4. **Run the Backend**

Ensure you are in the virtual environment and execute the Flask application.

```bash
python app.py
```

The application will be accessible at `http://0.0.0.0:5000/`.

### 5. **Frontend Setup**

The frontend is located in the `frontend/` folder and consists of static files served by Flask.

#### a. **Access the Application**

Open a web browser and navigate to `http://localhost:5000/`. The initial page will display the image capture interface.

#### b. **Camera Permissions**

Ensure that the browser has permission to access the device's camera. If prompted, allow camera access.

## 🌐 Deployment

To deploy the application, follow the basic steps below:

1. **Choose a Hosting Platform**
    - **Heroku:** A platform-as-a-service that supports Flask applications.
    - **AWS Elastic Beanstalk:** Amazon's service for deploying web applications.
    - **DigitalOcean:** VPS for hosting the application.

2. **Basic Production Configuration**
    - Use a web server like Gunicorn.
    - Configure necessary environment variables.
    - Ensure the database is configured for production.
