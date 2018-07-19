from flask import Flask, render_template, url_for, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://query:query@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

    def __repr__(self):
        return '<User %r>' % self.username



@app.route('/')
def index():
    results = Comments.query.all()
    return render_template('index.html', results=results)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))

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