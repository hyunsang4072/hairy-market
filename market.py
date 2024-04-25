from flask import Flask, render_template
# from markupsafe import escape

# create an instance of Flask
app = Flask(__name__)

# what URL should trigger this function
@app.route("/") # decorator
@app.route("/home")
def hello_world():
    return render_template("home.html")

@app.route("/about")
def about_me():
    return "<h1>Tell me about yourself!</h1>"

@app.route("/about/<username>")
def about_user(username):
    return f"<h1>Hi, there! {username}</h1>"
