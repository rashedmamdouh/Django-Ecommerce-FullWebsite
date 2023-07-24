document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('tshirtCanvas');
    const ctx = canvas.getContext('2d');
    const colorSwatches = document.querySelectorAll('.color-swatch');
    const imageUpload = document.getElementById('imageUpload');

    let tshirtColor = 'white';
    let uploadedImage;

    const img = new Image();
    img.onload = function() {
    ctx.drawImage(img, 0,0,400,400);
};
    img.src = '/style/images/blank_shirt_no_back.png';

    function drawTshirt() {
        ctx.fillStyle = tshirtColor;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        

        if (uploadedImage) {
            const imgX = (canvas.width - uploadedImage.width) / 2;
            const imgY = (canvas.height - uploadedImage.height) / 2;
            ctx.drawImage(uploadedImage, 85, 85, 245,315);
        }
    }

    // Change t-shirt color
    colorSwatches.forEach(swatch => {
        swatch.addEventListener('click', function () {
            tshirtColor = swatch.getAttribute('data-color');
            drawTshirt();
            ctx.drawImage(img, 0,0,400,400);
        });
    });

    // Upload image
    imageUpload.addEventListener('change', function (event) {
        const reader = new FileReader();

        reader.onload = function (e) {
            uploadedImage = new Image();
            uploadedImage.src = e.target.result;
            uploadedImage.onload = function () {
                drawTshirt();
                ctx.drawImage(img, 0,0,400,400);
            }
        };

        reader.readAsDataURL(event.target.files[0]);
    });

    drawTshirt();
});