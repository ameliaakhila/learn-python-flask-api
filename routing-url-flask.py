from flask import Flask

app = Flask(__name__)

@app.route("/")
def dasboard():
    return "<h1>Selamat datang di dasboard!</h1>"

@app.route("/home")
def home():
    return "<h1>Selamat datang di halaman utama!</h1>"

@app.route("/about")
def about():
    return "<h1>Selamat datang di halaman about!</h1>"  

@app.route("/contact")
def contact():
    return "<h1>Selamat datang di halaman contact!</h1>"

if __name__ == "__main__":
    app.run(debug=True)