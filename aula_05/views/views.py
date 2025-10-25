from main import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sac')
def sac():
    return render_template('sac.html')