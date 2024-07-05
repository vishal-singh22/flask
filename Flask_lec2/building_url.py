import time
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Welcome, to our home page!</h2>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1> congratz {sname.title()},you are passed with {marks} marks ready for treat!</h1>"
@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1> its okay {sname.title()},your marks is {marks} you can do much better !</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        time.sleep(1)
        return redirect(url_for("passed",sname=name,marks=num))

if __name__ == "__main__":
    app.run(debug=True)
