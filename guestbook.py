from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    return render_template('index.html', name=name, comment=comment)

@app.route('/home/<place>')
def home(place):
    return '<h1>You are on the ' + place + ' page!<?/h1>'

@app.route('/temp')
def temp():
    return render_template('example.html', myvar="variable I passed in")

@app.route('/links')
def links():
    links = ['https://www.youtube.com', 'https://reddit.com', 'https://www.bing.com']
    return render_template('example.html', links=links)
if __name__ == '__main__':
    app.run(debug=True)