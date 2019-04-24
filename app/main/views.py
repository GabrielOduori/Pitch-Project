from flask import render_template, redirect, url_for, abort
from . import main
from ..import db 
from .forms import PostForm, CommentForm
from ..models import User, Role, Post , Comment
from flask_login import login_required, current_user


@main.route('/',methods = ['GET', 'POST'])
# @login_required
def index():
    form_post = PostForm()
    if form_post.validate_on_submit():
        post = Post(body =form_post.body.data,
                    # author = current_user.username,
                    category = form_post.category.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form_post = form_post, posts = posts)
        


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user = user)


 
# @main.route('/post/<inti:id>')
# def post_comment(id):
#     post = Post.query.get_or_404
#     form = CommentForm
#     if form.validate_on_submit():
#         comment = Comment(body = form.body.data,
#                           post = post,
#                           author = current_user._get_current_object())
#         db.session.add(comment)
#         db.session.commit()
#         flash('You comments has been added.')
#         return redirect(url_for('.post', id=post.id, page = -1))