# app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    message = 'Добро пожаловать! version 2.0'
    return render_template('index.html', message=message)