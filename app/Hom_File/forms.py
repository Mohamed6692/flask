from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField


class Upload(FlaskForm):
    description = TextAreaField("TextArea", validators=[DataRequired()])
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Upload')


class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')
