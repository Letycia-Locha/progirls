from flask import Flask


app = Flask(__name__)

@app.route("/")

def home():
    return "A Progirls está online"

app.run(debug=True)