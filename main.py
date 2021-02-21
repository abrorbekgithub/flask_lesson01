import requests
import os
from tinydb import TinyDB
from flask import Flask

app=Flask(__name__)
@app.route('/')

def hello():
    return 'it is the first flask file'

app.run()