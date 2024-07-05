from flask import Flask

app =Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1> welcome back vishal </h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name.title()} welcome buddy how was your today!</h1>"

@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1> your input is {num} and the output is {num + 10}</h1>"

@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1,num2):
    return f"<h1> addition of {num1} + {num2} is {num1 + num2 }</h1>"


@app.route("/")
@app.route("/about")
def about():
    return "<h2> this is your about section VIshal !</h2>"
if __name__=="__main__":
    app.run(debug=True)