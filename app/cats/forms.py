from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from ..models import Categories

class CategoryForm(FlaskForm):
        category = StringField('Enter Your Category',validators=[Required()])
        submit = SubmitField('Add Category')

        

    


