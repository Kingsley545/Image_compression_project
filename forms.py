from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import InputRequired




class PostForm(FlaskForm):
    picture = FileField('Insert picture', validators=[InputRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submit')
