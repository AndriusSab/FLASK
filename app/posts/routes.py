from flask import render_template, request, url_for, redirect
from app.posts import bp
from app.extensions import db
from app.models.post import Post

@bp.route('/', methods = ("GET", "POST"))
def index():
    posts = Post.query.all()
    if request.method == "POST":
        new_post = Post(post=request.form["title"],
                        content =request.form["content"])
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('post.index'))
    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')



