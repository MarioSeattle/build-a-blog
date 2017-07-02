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

@app.route('/blog', methods=['GET', 'POST'])
def blog():
        title_error = ""
        content_error = ""

        blogs = Blog.query.all()
        return render_template('blog.html',blogs=blogs)

        if request.method == 'POST':
            blog_title = request.form['blog_title']
            blog_content = request.form['blog_content']

            if blog_title == '' and blog_content == '':
                return render_template('newPost.html', title_error=title_error, content_error=content_error)

            elif blog_title == '':
                return render_template('newPost.html', title_error=title_error, blog_content=blog_content)

            elif  blog_content == '':
                return render_template('newPost.html', content_error=content_error, blog_title=blog_title)
            
        return render_template('blog.html')

@app.route('/newPost', methods=['GET', 'POST'])
def newPost():
    blogs = Blog.query.all()
    return render_template('newPost.html',blogs=blogs)

#landing page redirected to blog
@app.route('/', methods=['GET'])
def index():
    return redirect('/blog') 

if __name__ == '__main__':
    app.run()