from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')
