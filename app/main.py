from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
        app.run(debug=True)    