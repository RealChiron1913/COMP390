document.querySelectorAll('.button, .button-control').forEach(button => {
    button.style.cursor = 'pointer'; // Change cursor to pointer when hover over buttons
    // Add click animation
    button.onmousedown = () => button.style.transform = 'scale(0.95)';
    button.onmouseup = () => button.style.transform = 'scale(1)';
});

document.getElementById('withoutkey').addEventListener('change', function() {
    var keyInput = document.getElementById('key');
    if (this.checked) {
        keyInput.disabled = true;
        keyInput.style.opacity = '0.5'; // Reduce opacity to indicate it's disabled
        // Smooth transition for opacity
        keyInput.style.transition = 'opacity 0.5s';
    } else {
        keyInput.disabled = false;
        keyInput.style.opacity = '1'; // Full opacity when enabled
    }
});

document.getElementById('ciphermethod').addEventListener('change', function() {
    var keyInput = document.getElementById('key');
    var method = this.value;
    var tooltip = document.querySelector('.info-icon');
    switch (method) {
        case 'caesar':
            tooltip = 'Caesar: Shifts letters by a fixed number.';
            break;
        case 'permutation':
            tooltip = 'Permutation: Rearranges letters according to a key.';
            break;
        case 'substitution':
            tooltip = 'Substitution: Replaces letters according to a key.';
            break;
    }
    var infoicon = document.querySelector('.info-icon');
    infoicon.setAttribute('data-tooltip', tooltip);
});

document.querySelectorAll('.info-icon').forEach(icon => {
    icon.addEventListener('mouseenter', function() {
        var tooltip = this.getAttribute('data-tooltip');
        var tooltipDiv = document.createElement('div');
        tooltipDiv.classList.add('tooltip');
        this.appendChild(tooltipDiv);
    });

    icon.addEventListener('mouseleave', function() {
        this.removeChild(this.querySelector('.tooltip'));
    });
});

function button_encrypt() {
    var plaintext = document.getElementById('plaintext').value;
    var key = document.getElementById('key').value;
    var language = document.getElementById('language').value;
    var ciphermethod = document.getElementById('ciphermethod').value;
    var casesensitive = document.getElementById('casesensitive').checked;
    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ plaintext: plaintext, key: key, language: language, ciphermethod: ciphermethod, casesensitive: casesensitive}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('ciphertext').value = data.ciphertext;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function saveTextAsFile(text, filename) {
    const blob = new Blob([text], {type: 'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename || 'download.txt';
    a.click();
    URL.revokeObjectURL(a.href);
}

document.getElementById('Plain-save').addEventListener('click', function() {
    var plaintext = document.getElementById('plaintext').value;
    saveTextAsFile(plaintext, 'plaintext.txt');
});

document.getElementById('Cipher-save').addEventListener('click', function() {
    var ciphertext = document.getElementById('ciphertext').value;
    saveTextAsFile(ciphertext, 'ciphertext.txt');
});

function uploadTextAsFile(inputElement) {
    const file = inputElement.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const text = e.target.result;
        if (inputElement.id === 'Plain-upload') {
            document.getElementById('plaintext').value = text;
        } else if (inputElement.id === 'Cipher-upload') {
            document.getElementById('ciphertext').value = text;
        }
    };
    reader.readAsText(file);
}

document.getElementById('Plain-upload').addEventListener('click', function() {
    var inputElement = document.createElement('input');
    inputElement.type = 'file';
    inputElement.accept = '.txt';
    inputElement.id = 'Plain-upload';
    inputElement.onchange = function() {
        uploadTextAsFile(this);
    };
    inputElement.click();
});







