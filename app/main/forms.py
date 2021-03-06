from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Categories
from wtforms import ValidationError

class PitchForm(FlaskForm):
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment =   TextAreaField('Add Your Comment Here...') 
    submit = SubmitField('Submit')

    


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
    
class Categories(FlaskForm):
    category = StringField('Category', validators=[Required()])
    submit = SubmitField('submit')
        