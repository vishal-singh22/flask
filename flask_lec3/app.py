from flask import Flask , render_template,url_for



#create the falsk app
app =Flask(__name__)


#this home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title= "Homes")


#this is about section
@app.route("/about")
def about():
    return render_template("about.html",title='About')


#start app
if __name__=="__main__":
    app.run(debug=True)