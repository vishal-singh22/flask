from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Welcome, to our home page!</h2>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1> welcome {name.title()} how was your today!</h1>"


if __name__ == "__main__":
    app.run(debug=True)