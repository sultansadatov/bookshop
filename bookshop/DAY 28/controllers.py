from flask import render_template
from app import app
from models import *

@app.route("/")
def home_page():
    book = Book.query.all()
    return render_template("index.html", page="home", book_var=book)

@app.route("/product/")
def product():
    return render_template("product.html", page="product")

@app.route("/book/<int:book_id>")
def book_page(book_id):
    book_details = Book.query.all()
    book_variable = book_details[book_id - 1]
    return render_template("book.html", book_var=book_variable)