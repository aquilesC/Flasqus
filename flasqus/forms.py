from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class CommentForm(FlaskForm):
    author_name = StringField('Display Name', validators=[InputRequired(), Length(min=1, max=128)])
    author_email = StringField('Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Message', validators=[InputRequired()])
    sign_up_newsletter = BooleanField('Sign Up to Newsletter')
    # recaptcha = RecaptchaField()
    submit = SubmitField('Send')