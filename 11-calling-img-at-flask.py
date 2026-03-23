from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Amelia Akhila"
    return render_template("index.html", nama_kirim=name)

if __name__ == "__main__":
    app.run(debug=True)