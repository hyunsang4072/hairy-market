from flask import Flask

# create an instance of Flask
app = Flask(__name__)

# what URL should trigger this function
@app.route("/") # decorator
def hello_world():
    return "<p>Hello, World!</p>"