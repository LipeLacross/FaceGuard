document.addEventListener("DOMContentLoaded", function() {
    const video = document.getElementById('camera');
    const canvas = document.getElementById('snapshot');
    const captureButton = document.getElementById('capture');

    // Tentar acessar a câmera do usuário
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
        .then(stream => {
            video.srcObject = stream;
            video.play();
        })
        .catch(() => {
            alert("Erro ao acessar a câmera. Verifique as permissões no navegador e tente novamente.");
        });

    // Capturar imagem quando o botão for clicado
    captureButton.addEventListener('click', () => {
        if (!video.srcObject) {
            alert("Câmera não está ativa. Verifique as permissões.");
            return;
        }

        // Capturar a imagem do vídeo
        const context = canvas.getContext('2d');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Converter a imagem em base64 e enviar para o backend
        const dataURL = canvas.toDataURL('image/png');
        sendImage(dataURL);
    });

    // Função para enviar a imagem ao backend
    function sendImage(dataURL) {
        const url = window.location.hostname === 'localhost' ? 'http://127.0.0.1:5000/upload' : `http://${window.location.hostname}:5000/upload`;

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: dataURL }),
        })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(errorData => {
                        throw new Error(errorData.error);
                    });
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    alert(`Erro do servidor: ${data.error}`);
                } else {
                    alert("Reconhecimento feito com sucesso!");
                }
            })
            .catch(error => {
                alert(`Erro ao enviar a imagem ao servidor: ${error.message}`);
            });
    }
});
