from datetime import datetime
from hashlib import md5

from flasqus import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(128), nullable=False)
    author_email = db.Column(db.String(156), nullable=False)
    message = db.Column(db.Text)
    sign_up_newsletter = db.Column(db.Boolean, default=False)
    needs_moderation = db.Column(db.Boolean, default=False)
    thread_id = db.Column(db.String(256), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def gravatar(self):
        code = md5(self.author_email.encode('ascii')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon'.format(code)