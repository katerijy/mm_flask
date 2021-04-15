import os, base64
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import UserMixin
from app import routes


# @login.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    mymcard = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<User: {self.username} | {self.email}>'

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

class Mymcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mymcard = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, nullable=False)
    

    def __init__(self, mymcard, user_id):
        self.mymcard = mymcard
        self.user_id = user_id

    def __repr__(self):
        return f'<Your Meditation Card: {self.mymcard}>'

    def to_dict(self):
        return {
            'id': self.id,
            'mymcard': self.mymcard,
            'date_created': self.date_created,
            'user': User.query.get(self.user_id).username
        }

class Mcards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meridian = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    emotions = db.Column(db.String(50), nullable=False)
    taste = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    def __init__(self, meridian, time, climate, taste, emotions, location):
        self.time = time
        self.meridian = meridian
        self.climate = climate
        self.emotions = emotions
        self.location = location
    
    def to_dict(self):
        return {
            'id': self.id,
            'time': self.time,
            'climate': self.climate,
            'emotions': self.emotions,
            'location': self.location,
            'meridian': self.meridian,
        }
        
   


    
    