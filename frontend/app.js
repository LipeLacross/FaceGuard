document.addEventListener("DOMContentLoaded", function() {
    const video = document.getElementById('camera');
    const canvas = document.getElementById('snapshot');
    const captureButton = document.getElementById('capture');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        });

    captureButton.addEventListener('click', () => {
        const context = canvas.getContext('2d');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        const dataURL = canvas.toDataURL('image/png');
        sendImage(dataURL);
    });

    function sendImage(dataURL) {
        fetch('http://localhost:5000/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: dataURL }),
        }).then(response => response.json())
            .then(data => {
                console.log(data);
            });
    }
});
