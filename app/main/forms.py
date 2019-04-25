from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators, TextAreaField, SelectField
from wtforms.validators import Required
from ..models import Post, User

class PostForm(FlaskForm):
    body = TextAreaField("What's your biggest idea?", validators=[Required()])
    category = SelectField("Category",choices=([('technology','Technology'),
                                                 ('fashion','Fashion'),
                                                 ('hospitality','Hospitality'),
                                                 ('government','Government')
                                                 ]) ,validators=[Required()])

    submit = SubmitField('Submit pitch')

    
class CommentForm(FlaskForm):
    body = StringField('', validators=[Required()])
    submit = SubmitField('Submit')
    
    
    
    
