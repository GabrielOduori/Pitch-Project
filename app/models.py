
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
# from email import send_email


'''
Creating a model that will hold all the classes for the key entities
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'Role {self.name}'

class User(UserMixin,db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index =True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'author', lazy = "dynamic")
    posts = db.relationship('Post', backref = 'author', lazy = "dynamic")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
 
    
    '''
    This part of the code is to implement a token system
    that would be used to send emails to an email account
    and the user confirms before being added to the list
    '''
    def generate_confirmation_token(self,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})
    
    def confirm(self,token):
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
    
    
class Post(db.Model):
    __tablename__ = 'posts'
    id  = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    
    


         

    
    
class Comment(db.Model):
    __tablename__='comments'
    id  = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    

        

    
    
    