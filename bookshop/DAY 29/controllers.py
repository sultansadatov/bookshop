from flask import render_template, request, redirect
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from app import app
from models import *
from forms import LoginForm, RegistrationForm, UserForm
from datetime import datetime

@app.route("/")
def home_page():
    book = Book.query.all()
    return render_template("index.html", page="home", book_var=book)

@app.route("/product/")
def product():
    book_details = Book.query.all()[0]
    return render_template("product.html", page="product", book_var=book_details)

@app.route("/book/<int:book_id>", methods=["GET", "POST"])
def book_page(book_id):
    book_details = Book.query.all()
    book_variable = book_details[book_id - 1]
    message = Comments.query.filter(Comments.book_id == book_id).all()
    post_data = request.form
    print(post_data)
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data=post_data)
        if form.validate_on_submit():
            comment = Comments(full_name=form.full_name.data, message=form.message.data, time=datetime.now(), book_id=book_id)
            comment.save()
    return render_template("book.html", book_var=book_variable, form=form, comments=message)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    post_data = request.form
    if request.method == "POST":
        form = RegistrationForm(data=post_data)
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            user.save()
            return redirect("/login")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.form)
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect("/")
            else:
                print("Unsuccesfull")
    return render_template("login.html", form=form)

@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect("/login")