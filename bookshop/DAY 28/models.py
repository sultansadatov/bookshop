from extensions import *

class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    price = db.Column(db.Integer(), default=10)
    description = db.Column(db.String(255), default="Some text")
    image_url = db.Column(db.String(255), nullable=True)
    stock = db.Column(db.Integer(), nullable=True)
    genre = db.Column(db.String(255), nullable=True)
    lang = db.Column(db.String(50), default="English")
    publisher = db.Column(db.String(100), nullable=True)

    # def __init__(self, title, author, price, description, image_url, stock, genre, lang, publisher):
    #     self.title = title
    #     self.author = author
    #     self.price = price
    #     self.description = description
    #     self.image_url = image_url
    #     self.stock = stock
    #     self.genre = genre
    #     self.lang = lang
    #     self.publisher = publisher

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()