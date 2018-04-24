from flask import render_template, request
from sqlalchemy import desc
from flask_cors import cross_origin

from flasqus import app, db
from .forms import CommentForm
from .models import Comment

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_comment', methods=['GET', 'POST'])
@cross_origin(origin='*')
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(author_name=form.author_name.data,
                          author_email=form.author_email.data,
                          message=form.message.data,
                          thread_id=1)

        db.session.add(comment)
        db.session.commit()
        return 'Message received', 200
    return render_template('new_comment.html', form=form)


@app.route('/add_comment', methods=['POST'])
def add_comment():
    print('Here')
    form = CommentForm()
    if form.validate_on_submit():
        print('Validated Form')
        return 'OK', 200
    data = request.get_json(cache=False)
    user = request.form['author_name'];
    print(user)
    return 'OK', 200

@app.route('/view_comments/<thread_id>')
@cross_origin(origin='*',headers=['Content-Type','Authorization'], methods=['GET'])
def view_comment(thread_id):
    comments = Comment.query.filter_by(thread_id=thread_id).all()
    return render_template('thread.html', comments=comments)