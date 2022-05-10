# import email
from email.policy import default
from flask import Flask, render_template, flash,redirect, url_for
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

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
    form = RegistrationForm() 
    if form.validate_on_submit():
        flash(f' Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        if form.email.data == 'abby@gmail.com' and form.password.data == '1234word':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

