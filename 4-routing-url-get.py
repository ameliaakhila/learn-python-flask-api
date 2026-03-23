from flask import Flask, request

app = Flask(__name__)
@app.route("/search")
def search():
    keywords = request.args.get("keyword", "tidak ada keyword yang diberikan")
    page = request.args.get("page", "1")
    return f"<h1>Search Results: {keywords}</h1> <p>Page: {page}</p>"

if __name__ == "__main__":
    app.run(debug=True)