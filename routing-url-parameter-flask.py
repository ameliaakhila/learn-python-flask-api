from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Hallo, aku sedang belajar Flask!</h1>"

@app.route("/user/<username>/<umur>/<pekerjaan>")
def show_user_profile(username, umur, pekerjaan):
    return f"<h1>Profil pengguna: {username},<br> Umur: {umur},<br> Pekerjaan: {pekerjaan}</h1>"
if __name__ == "__main__":
    app.run(debug=True)