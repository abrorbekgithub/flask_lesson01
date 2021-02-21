import requests
import os
from tinydb import TinyDB
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/home')
def home():
    return 'home page'
    
app.run(debug=True)