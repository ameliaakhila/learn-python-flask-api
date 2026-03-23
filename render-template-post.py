from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    return f"<h1>Selamat Datang, {name}!</h1><h2>Umur Anda adalah {age} tahun.</h2>"

if __name__ == "__main__":
    app.run(debug=True)