from extensions import db, login_manager
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(50))
    message = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    book_id = db.Column(db.Integer(), nullable=False)


    def __init__(self, full_name, message, time, book_id):
        self.full_name = full_name
        self.message = message
        self.time = time
        self.book_id = book_id

    def __repr__(self):
        return self.full_name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(50), default=10, nullable=False)
    description = db.Column(db.String(255), default="Some text", nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    lang = db.Column(db.String(50), default="English")
    publisher = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author, price=12, description="Some text", image_url="/static/images/Inkognito.png", stock=2, genre="Psychology", lang="English", publisher="Qanun nesriyyat"):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.genre = genre
        self.lang = lang
        self.publisher = publisher

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, email, password, is_active=True, is_superuser=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_active = is_active
        self.is_superuser = is_superuser

    def __repr__(self):
        return self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

# 12	Some text	/static/images/Inkognito.png	2	Psychology	English	Qanun nesriyyat  evi