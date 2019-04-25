from threading import Thread
from flask_mail import Message
from flask import render_template, current_app
from . import mail
from config import Config

def send_async_email(app,email):
    with app.app_context():
        mail.send(email)

def mail_message(subject,template,to,**kwargs):
        app = current_app._get_current_object()
        sender_email = Config.MAIL_USERNAME
        email = Message(subject, sender=sender_email, recipients=[to])
        email.body = render_template(template + '.txt', **kwargs)
        email.html = render_template(template + '.html', **kwargs)
        thread = Thread(target=send_async_email,args=[app,email])
        thread.start()
        return thread
