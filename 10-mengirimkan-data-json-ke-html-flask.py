from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    user = [
        {"nama": "Amelia Akhila", "email": "amelia@example.com", "pekerjaan": "Mahasiswa"},
        {"nama": "John Doe", "email": "john@example.com", "pekerjaan": "Software Engineer"},
        {"nama": "Jane Smith", "email": "jane@example.com", "pekerjaan": "Data Analyst"},
        {"nama": "Bob Johnson", "email": "bob@example.com", "pekerjaan": "Project Manager"}
    ]
    return render_template("user.html", data_user=user)

if __name__ == "__main__":
    app.run(debug=True)