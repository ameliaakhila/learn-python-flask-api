from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "nama": "Amelia Akhila",
        "umur": 20,
        "pekerjaan": "Mahasiswa"
    }
    return render_template("biodata/index.html", **data)

if __name__ == "__main__":
    app.run(debug=True)