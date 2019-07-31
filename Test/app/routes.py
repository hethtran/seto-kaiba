from flask import Flask, render_template, request, redirect, Response
import random, json
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Leif'}
    return render_template('index.html', title='Home', user=user)

@app.route('/chess')
def chess():
    return render_template('tests.html')
