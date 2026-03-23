// ===== Navigation Functionality =====
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initPredictionForm();
});

// Initialize sidebar navigation
function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.content-section');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            // Get section id from data attribute
            const sectionId = this.getAttribute('data-section');
            const targetSection = document.getElementById(sectionId);

            // Remove active class from all links and sections
            navLinks.forEach(l => l.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));

            // Add active class to clicked link and corresponding section
            this.classList.add('active');
            if (targetSection) {
                targetSection.classList.add('active');
                // Scroll to top of content
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        });
    });
}

// ===== Prediction Form Functionality =====
function initPredictionForm() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('prediction-result');

    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Get form values
        const umur = document.getElementById('umur').value;
        const luas = document.getElementById('luas').value;
        const kamar = document.getElementById('kamar').value;

        // Validate inputs
        if (!umur || !luas || !kamar) {
            showError('Semua field harus diisi!');
            return;
        }

        // Show loading state
        const submitBtn = form.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Loading...';
        submitBtn.disabled = true;

        try {
            // Call API
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    umur_rumah: parseFloat(umur),
                    luas_tanah: parseFloat(luas),
                    jumlah_kamar: parseFloat(kamar)
                })
            });

            const data = await response.json();

            if (response.ok) {
                // Show success result
                showPredictionResult(data.pesan, data.harga_prediksi, 'success');
            } else {
                // Show error result
                showPredictionResult(data.pesan, null, 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showPredictionResult('Terjadi kesalahan saat menghubungi server', null, 'error');
        } finally {
            // Reset button state
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

// Show prediction result
function showPredictionResult(message, harga, type) {
    const resultDiv = document.getElementById('prediction-result');
    const resultText = document.getElementById('prediction-text');
    const resultBox = document.querySelector('.result-box');

    if (type === 'success') {
        resultText.innerHTML = `
            <strong>✅ Prediksi Berhasil!</strong><br>
            ${message}<br>
            <span style="font-size: 1.3em; color: #1b5e20;">Rp ${formatCurrency(harga)}</span>
        `;
        resultBox.style.background = 'linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)';
        resultBox.style.borderLeftColor = '#4caf50';
    } else {
        resultText.innerHTML = `
            <strong>❌ Prediksi Gagal</strong><br>
            ${message}
        `;
        resultBox.style.background = 'linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)';
        resultBox.style.borderLeftColor = '#f44336';
    }

    resultDiv.style.display = 'block';
    // Scroll to result
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Format currency (Rupiah)
function formatCurrency(value) {
    return new Intl.NumberFormat('id-ID', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(value);
}

// Show error message
function showError(message) {
    alert(message);
}

// ===== Utility Functions =====

// Load contoh data from API
async function loadExampleData() {
    try {
        const response = await fetch('/api/contoh-data');
        const data = await response.json();
        console.log('Contoh Data:', data);
        return data;
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

// Syntax highlighting helper (optional)
function highlightCode() {
    const codeBlocks = document.querySelectorAll('.code-block code');
    codeBlocks.forEach(block => {
        // Simple color coding for common keywords
        let text = block.textContent;
        text = text.replace(/\b(from|import|def|class|if|else|for|while|return|try|except)\b/g, '<span style="color: #d4af37;">$1</span>');
        // This is simplified; untuk production gunakan library seperti Highlight.js
    });
}

// Copy code to clipboard
function copyCodeToClipboard(button) {
    const codeBlock = button.nextElementSibling;
    const code = codeBlock.querySelector('code').textContent;

    navigator.clipboard.writeText(code).then(() => {
        const originalText = button.textContent;
        button.textContent = '✓ Copied!';
        setTimeout(() => {
            button.textContent = originalText;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// ===== Event Listeners =====

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Alt + G untuk go to top
    if (e.altKey && e.key === 'g') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
});

// Log when page loads
console.log('%cFlask Documentation App Loaded', 'color: #0277bd; font-size: 14px; font-weight: bold;');
console.log('Ready to learn Flask! Start by exploring the sidebar menu.');
