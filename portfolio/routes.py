from portfolio import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='project')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')