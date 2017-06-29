from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:sounders@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/newPost', methods=['GET', 'POST'])
def newPost():

@app.route('/singleEentry', methods=['GET'])
def singleEntry():

@app.route('/blog', methods=['GET'])
def blog():

@app.route('/', methods=['GET'])
def index():
  
    



if __name__ == '__main__':
    app.run()