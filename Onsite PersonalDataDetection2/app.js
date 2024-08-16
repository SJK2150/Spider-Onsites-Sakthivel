document.getElementById('uploadButton').addEventListener('click', async () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a file first.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();  
            document.getElementById('resultText').textContent = JSON.stringify(result, null, 2);
        } else {
            alert('Failed to analyze the file.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred.');
    }
});
