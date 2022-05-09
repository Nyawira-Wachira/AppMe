from flask import Flask, render_template, flash,redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0b6bd163c27f7d7512077a91'

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

@app.route('/Login')
def login():
    form = LoginForm() 
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
        app.run(debug=True)    