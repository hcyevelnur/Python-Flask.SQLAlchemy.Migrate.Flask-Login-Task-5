from extensions import db   
from extensions import * 
from flask_login import UserMixin  
from werkzeug.security import generate_password_hash, check_password_hash
from app import *




class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    comment = db.Column(db.String(100))

    def __repr__(self):
        return self.full_name

    def __init__(self, full_name, email, phone, comment):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.comment = comment

    def save(self):
        db.session.add(self)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    is_active = db.Column(db.Boolean, nullable = False)
    is_superuser = db.Column(db.Boolean, nullable = False)

    def __repr__(self):
        return self.name

    def __init__(self, name, last_name, username, email, phone, password, is_active=True, is_superuser=True):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password)
        self.is_active = is_active
        self.is_superuser = is_superuser


    def save(self):
        db.session.add(self)
        db.session.commit()

    
    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def chech_password(self, password):
        return check_password_hash(self.password, password)
