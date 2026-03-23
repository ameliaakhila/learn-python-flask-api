from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    is_logged_in = True
    nama = "Amelia Akhila"
    items = ["Mangga", "Pisang", "Apel"]
    return render_template("index1.html", nama_kirim=nama, logged_in=is_logged_in, items_list=items)

@app.route("/logout", methods=["POST"])
def logout():
    is_logged_in = False
    nama = "Tamu"
    items = ["Tidak ada item yang tersedia"]
    return render_template("index1.html", nama_kirim=nama, logged_in=is_logged_in, items_list=items)

if __name__ == "__main__":
    app.run(debug=True)