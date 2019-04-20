
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

'''
Creating a model that will hold all the classes for the key entities
'''

class User(db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index =True)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    comment = db.relationship('Comment', backref = 'users', lazy = "dynamic")
    pitches  = db.relationship('Pitch', backref = 'users', lazy = "dynamic")
    
    def __init__(self,username):
        self.username = username

    
    def __repr__(self):
        return f'User {self.username}'
    
    @property
    def password(self):
        raise AttributeError('You can  not read the password attribute')
    
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
class PitchCategory(db.Model):
    __tablename__='pitch_category'
    id  = db.Column(db.Integer, primary_key = True)
    description = db.String(db.String)
    categories  = db.relationship('PitchCategory', backref = 'pitches', lazy = "dynamic")
    
    def __init__(self,description):
        self.description = description
    
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id  = db.Column(db.Integer, primary_key = True)
    pitch_text = db.Column(db.String)
    posted_on = db.Column(db.DateTime, default = datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category  = db.relationship('PitchCategory', backref = 'pitches', lazy = "dynamic")
    
#     def __init__(self,pitch_text,user_id):
#         self.pitch_text = pitch_text
#         self.user_id = user_id
        

#     def save_pitch(self):
#         db.session.add(self)
#         db.session.commit()
        
         
#     @classmethod
#     def get_pitches(cls,id):
#         pitches = Pitch.query.filer_by(pitch_id = id).all()
#         return pitches
    
    
# class Comment(db.Model):
#     __tablename__='comments'
#     id  = db.Column(db.Integer, primary_key = True)
#     comment_text = db.Column(db.String)
#     comment_date = db.Column(db.DateTime, default = datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     pitch_id = db.Column(db.Integer, db.ForeignKey("pitch.id"))
    
#     def __init__(self,comment_date,comment_text,user_id,pitch_id):
#         self.comment_text = comment_text
#         self.comment_date = comment_date
#         self.user_id = user_id
#         self.pitch_id = pitch_id
    
    
#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()
        
        
#     @classmethod
#     def get_comments(cls,id):
#         comments = Comment.query.filer_by(pitch_id = id).all()
#         return comments
    
    
    
    