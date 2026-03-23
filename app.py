from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Route untuk halaman dokumentasi
@app.route("/")
def home():
    return render_template("documentation/index.html")

# API endpoint untuk contoh prediksi sederhana
@app.route("/api/predict", methods=["POST"])
def predict():
    """
    API endpoint untuk prediksi sederhana menggunakan ML
    Contoh: Prediksi harga berdasarkan fitur input
    """
    try:
        data = request.get_json()
        
        # Contoh fitur: umur_rumah, luas_tanah, jumlah_kamar
        umur_rumah = float(data.get('umur_rumah', 0))
        luas_tanah = float(data.get('luas_tanah', 0))
        jumlah_kamar = float(data.get('jumlah_kamar', 0))
        
        # Model prediksi sederhana (bukan ML sejati, hanya untuk demo)
        # Formula: harga = (luas_tanah * 100000) + (jumlah_kamar * 50000) - (umur_rumah * 5000)
        harga = (luas_tanah * 100000) + (jumlah_kamar * 50000) - (umur_rumah * 5000)
        
        return jsonify({
            'status': 'success',
            'harga_prediksi': round(harga, 2),
            'pesan': f'Prediksi harga rumah: Rp {harga:,.0f}'
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'pesan': f'Terjadi kesalahan: {str(e)}'
        }), 400

# API endpoint untuk contoh data
@app.route("/api/contoh-data", methods=["GET"])
def contoh_data():
    """API endpoint untuk mendapatkan data contoh"""
    data = {
        'status': 'success',
        'data': [
            {'id': 1, 'nama': 'Python', 'tipe': 'Bahasa Pemrograman'},
            {'id': 2, 'nama': 'Flask', 'tipe': 'Web Framework'},
            {'id': 3, 'nama': 'Machine Learning', 'tipe': 'Bidang AI'},
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)