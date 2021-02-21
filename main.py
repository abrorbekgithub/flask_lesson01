import requests
import os
from tinydb import TinyDB
from flask import Flask

app=Flask(__name__)

html='''
<!DOCTYPE html>
<html>
<body>

<h1>Computer Code</h1>
<h3> <p>Some programming code:</p> </h3>

<code>
x = 5;
y = 6;
z = x + y;
</code>

</body>
</html>
'''

@app.route('/')
def hello():
    return 'hello'

@app.route('/home')
def home():
    return html

@app.route('/index')
def index():
    return "index"


app.run(debug=True)