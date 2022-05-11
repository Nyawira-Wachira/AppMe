from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail,Message


app = Flask(__name__)

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')
            

    return render_template("login.html", user=current_user)


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            mail = Mail(app)
            msg = Message('Hello, Welcome to AppMe.', sender = 'abigail.nyawira22@gmail.com', recipients = ['abigailwachira@gmail.com'])
            msg.body = "Your account has been created successfully!"
            # mail.send(msg)
            flash('Account created successfully and Email sent!', 'success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)


@auth.route("/tech")
@login_required
def tech():
    return render_template("tech.html")

@auth.route("/hero")
@login_required
def hero():  
    return render_template("hero.html") 
    
@auth.route("/quotes")
@login_required
def quotes():  
    return render_template("quotes.html") 


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))