from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators, TextAreaField
from wtforms.validators import Required

class PostForm(FlaskForm):
    body = TextAreaField("What's your biggest idea?", validators=[Required()])
    submit = SubmitField('Submit pitch')
    
    
# class DeleteForm(FlaskForm):
#     id = IntegerField("Id of the pitch to be removed")
#     submit = SubmitField('Remove pitch')
    
    
class CommentForm(FlaskForm):
    body = StringField('', validators=[Required()])
    submit = SubmitField('Submit')
    
    
    
    
