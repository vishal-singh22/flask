import time
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Welcome, to our home page!</h2>"

@app.route("/pass")
def passed():
    return "<h1> congratz,you are passed ready for treat!</h1>"
@app.route("/fail")
def failed():
    return "<h1> its okay, you can do much better !</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        return redirect(url_for("passed"))

if __name__ == "__main__":
    app.run(debug=True)
