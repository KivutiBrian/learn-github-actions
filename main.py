from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/about')
def about():
    return "learning all about github actions"

@app.route('/<page_name>')
def other_page(page_name):
    res = make_response(f"The page {page_name} does not exist", 404)
    return res