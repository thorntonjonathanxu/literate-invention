from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SampleForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    favoritecolor = StringField('Favorite Color', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')