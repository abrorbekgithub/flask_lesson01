import requests
import os
from tinydb import TinyDB
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/home')
def home():
    return 'home'

@app.route('/latest')
def latest():
    return 'latest'

if __name__ == "__main__":
    app.run(debug=True)

