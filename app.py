from flask import Flask, render_template, jsonify, Response, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.id

@app.route('/') #could add methods post and get
def index_view():
    username = request.args.get('username')
    #this loads the webpage from template file
    return render_template('index.html', username = username)

@app.route('/timeline')
def timeline_view():
    return render_template('timeline.html')

@app.route('/users')
def users_view():
    with open('./users.json', 'r') as f:
        users = f.read()
    return Response(users, mimetype="application/json")

@app.route('/posts')
def posts_view():
    with open('./posts.json', 'r') as f:
        posts = f.read()
    return Response(posts, mimetype="application/json")

@app.route('/test')
def test_view():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')