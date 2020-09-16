from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, StringField
from wtforms.validators import DataRequired, ValidationError

class EntryForm(FlaskForm):
    title = StringField('Text', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    is_published = BooleanField('Is_Published', validators=[DataRequired()], default="checked")
  