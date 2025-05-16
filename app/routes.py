from flask import render_template, redirect, url_for
import app
from app import main, db

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')