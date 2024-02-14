// Event listeners for UI interactions
function initializeEventListeners() {
    document.querySelectorAll('.button, .button-control').forEach(button => {
        button.style.cursor = 'pointer';
        button.onmousedown = () => button.style.transform = 'scale(0.95)';
        button.onmouseup = () => button.style.transform = 'scale(1)';
    });

    document.getElementById('withoutkey').addEventListener('change', toggleKeyInput);
    document.getElementById('ciphermethod').addEventListener('change', updateTooltip);
    document.getElementById('Plain-save').addEventListener('click', () => saveText('plaintext'));
    document.getElementById('Cipher-save').addEventListener('click', () => saveText('ciphertext'));
    document.getElementById('Plain-upload').addEventListener('click', () => uploadText('plaintext'));
    document.getElementById('Cipher-upload').addEventListener('click', () => uploadText('ciphertext'));
}

// Toggle key input based on checkbox
function toggleKeyInput() {
    var keyInput = document.getElementById('key');
    keyInput.disabled = this.checked;
    keyInput.style.opacity = this.checked ? '0.5' : '1';
    keyInput.style.transition = 'opacity 0.5s';
}

// Update tooltip for cipher method
function updateTooltip() {
    var tooltip = getTooltipByMethod(this.value);
    document.querySelector('.info-icon').setAttribute('data-tooltip', tooltip);
}

// Get tooltip text by cipher method
function getTooltipByMethod(method) {
    switch (method) {
        case 'caesar': return 'Caesar: Shifts letters by a fixed number.';
        case 'permutation': return 'Permutation: Rearranges letters according to a key.';
        case 'substitution': return 'Substitution: Replaces letters according to a key.';
        default: return '';
    }
}

// Save text from specified textarea
function saveText(areaId) {
    var text = document.getElementById(areaId).value;
    var filename = areaId + '.txt';
    saveTextAsFile(text, filename);
}

// Upload text to specified textarea
function uploadText(areaId) {
    var inputElement = document.createElement('input');
    inputElement.type = 'file';
    inputElement.accept = '.txt';
    inputElement.onchange = function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById(areaId).value = e.target.result;
            };
            reader.readAsText(file);
        }
    };
    inputElement.click();
}

// Utility function to save text as a file
function saveTextAsFile(text, filename) {
    const blob = new Blob([text], {type: 'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}

// Encrypt button click event
function button_click(textContent) {
    var plaintext = document.getElementById('plaintext').value;
    var ciphertext = document.getElementById('ciphertext').value;
    var key = document.getElementById('key').value;
    var language = document.getElementById('language').value;
    var ciphermethod = document.getElementById('ciphermethod').value;
    var casesensitive = document.getElementById('casesensitive').checked;
    var withoutKey = document.getElementById('withoutkey').checked;
    var keyprocess = document.getElementById('keyprocess').checked;
    if (textContent == "Encrypt") {
        encrypt(plaintext, key, ciphermethod, language, casesensitive, withoutKey, keyprocess);
    } else {
        decrypt(ciphertext, key, ciphermethod, language, casesensitive, withoutKey, keyprocess);
    }
}

function encrypt(plaintext, key, ciphermethod, language, casesensitive, withoutKey, keyprocess) {
    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ plaintext: plaintext, key: key, language: language, ciphermethod: ciphermethod, casesensitive: casesensitive, withoutKey: withoutKey, keyprocess: keyprocess}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('ciphertext').value = data.ciphertext;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function decrypt(ciphertext, key, ciphermethod, language, casesensitive, withoutKey, keyprocess) {
    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ciphertext: ciphertext, key: key, language: language, ciphermethod: ciphermethod, casesensitive: casesensitive, withoutKey: withoutKey, keyprocess: keyprocess}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('plaintext').value = data.plaintext;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Initialize event listeners on document load
document.addEventListener('DOMContentLoaded', initializeEventListeners);
