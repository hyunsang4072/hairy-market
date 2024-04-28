from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # backref: reference to a string relationship name, or a backref() construct,
    # which will be used to automatically generate a new relationship() on the related class
    # lazy=True: select - items should be loaded lazily when the property is first accessed,
    # using a separate SELECT statement, or identity map fetch for simple many-to-one references
    items = db.relationship('Item', backref='owned_user', lazy=True)    # using SELECT statement

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    # ForeignKey(): searches for the primary_key; a marker object that defines a dependency between two columns
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item: {self.name}"