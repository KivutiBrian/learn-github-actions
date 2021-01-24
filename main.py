from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/about')
def about():
    return "learning all about github actions"