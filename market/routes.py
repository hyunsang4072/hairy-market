from market import app
from flask import render_template
from market.models import Item

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

@app.route('/market')
def market_page():
    # items = [
    # {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    # {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    # {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    items = Item.query.all()
    return render_template('market.html', items=items)
