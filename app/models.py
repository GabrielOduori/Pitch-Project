
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer
from flask import current_app
# from email import send_email


'''
Creating a model that will hold all the classes for the key entities
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__  = 'roles'
    id  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    # default = db.Column(db.Boolean, default=False, index=True)
    # permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy = "dynamic")
    
    def __repr__(self):
        return f'Role {self.name}'
    
    
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0
class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

class User(UserMixin,db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index =True)
    username = db.Column(db.String(255))
    # bio = db.Column(db.String(255))
    # profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    # comment = db.relationship('Comment', backref = 'users', lazy = "dynamic")
    # pitches  = db.relationship('Pitch', backref = 'users', lazy = "dynamic")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean, default = False)
    
    
    def generate_confirmation_token(self,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})
    
    def confim(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm')!=self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    
    # def __init__(self,username):
    #     self.username = username

    
    def __repr__(self):
        return f'User {self.username}'
    
    @property
    def password(self):
        raise AttributeError('You can  not read the password attribute')
    
    
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
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
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
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
    
    
    
    