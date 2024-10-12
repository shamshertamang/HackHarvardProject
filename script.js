document.getElementById('upload-button').addEventListener('click', function() {
    const fileInput = document.getElementById('file-upload');
    const resultDiv = document.getElementById('result');

    if (fileInput.files.length === 0) {
        resultDiv.innerHTML = '<p style="color: red;">Please upload an image.</p>';
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        // Display uploaded image
        const img = document.createElement('img');
        img.src = e.target.result;
        img.style.maxWidth = '100%';
        img.style.borderRadius = '8px';
        resultDiv.innerHTML = ''; // Clear previous results
        resultDiv.appendChild(img);

        // Here, you would typically send the image to your backend for processing
        // For demonstration, let's just show a placeholder result
        const placeholderResult = document.createElement('p');
        placeholderResult.innerText = 'This is a placeholder for your sorting result.';
        resultDiv.appendChild(placeholderResult);
    };

    reader.readAsDataURL(file);
});
