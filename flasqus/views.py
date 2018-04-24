from flask import render_template, request
from sqlalchemy import desc
from flask_cors import cross_origin

from flasqus import app, db, csrf
from .forms import CommentForm
from .models import Comment

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_comment', methods=['GET', 'POST'])
@cross_origin()
@csrf.exempt
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(author_name=form.author_name.data,
                          author_email=form.author_email.data,
                          message=form.message.data,
                          thread_id=1)

        db.session.add(comment)
        db.session.commit()
        return render_template('message_received.html')
    return render_template('new_comment.html', form=form)

@app.route('/view_comments/<thread_id>')
@cross_origin()
def view_comment(thread_id):
    comments = Comment.query.filter_by(thread_id=thread_id).all()
    return render_template('thread.html', comments=comments)