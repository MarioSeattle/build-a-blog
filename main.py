from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:sounders@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))
    def __init__(self, title, body):
        self.title = title
        self.body = body
@app.route('/blog', methods=['GET', 'POST'])
def index():
    if 'id' in request.args:
        return single_blog()
    else:
        blogs = Blog.query.all()
        return render_template('blog.html', title="Build A Blog", 
            blogs=blogs)
@app.route('/newPost', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'GET':
        return render_template('newPost.html', title="Add Blog Entry")
    if request.method == 'POST':
        blog_title = request.form['blog']
        blog_body = request.form['blog_body']
        title_error = ""
        body_error = ""
        if len(blog_title) < 1:
            title_error = "Please fill in the title"
        if len(blog_body) < 1:
            body_error = "Please fill in the body"

        if not title_error and not body_error:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            query_param_url = "/blog?id=" + str(new_blog.id)
            return redirect(query_param_url)
            # or: return render_template('singleBlogEntry.html', blog=blog)
        else:
            return render_template('newPost.html', title="Add Blog Entry", 
                title_error=title_error, body_error=body_error)

def single_blog():

    blog_id = int(request.args.get('id'))
    single_blog = Blog.query.get(blog_id)

    return render_template('singlePost.html',id=single_blog.id, title=single_blog.title,body=single_blog.body)


if __name__ == '__main__':
    app.run()