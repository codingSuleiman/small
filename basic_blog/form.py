from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo, ValidationError, Regexp


class PostForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()], render_kw={"placeholder": "Send an anonymous message"})

class TotalPost(FlaskForm):
    total_posts = []