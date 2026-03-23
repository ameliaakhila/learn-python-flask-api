from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    nama = "Amelia Akhila"
    return render_template("index.html", nama_kirim=nama)

if __name__ == "__main__":
    app.run(debug=True)