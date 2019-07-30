from flask import render_template, url_for
from app import app

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/chess')
def chess():
    return render_template('tests.html')
