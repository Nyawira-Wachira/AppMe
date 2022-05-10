# import email
from email.policy import default
from flask import Flask, render_template, flash,redirect, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# app = Flask(__name__)

posts = [
    {
        'author': 'Linda Jones',
        'title': 'First Pitch',
        'description' : 'First Pitch description',
        'date_posted': 'May 6, 2022'
    },
    {
        'author': 'Peter Woo',
        'title': 'SecondPitch',
        'description' : '   Second Pitch description',
        'date_posted': 'May 7, 2022'
    },
    {
        'author': 'Bradley Smith',
        'title': 'Third Pitch',
        'description' : 'Third Pitch description',
        'date_posted': 'May 8, 2022'
    }
]

@app.route('/')
def home():
    return render_template('home.html',posts=posts) 

@app.route('/movies')
def movies():
    return render_template('movie.html',title='Movies') 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm() 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. You can Login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm() 
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
       
