from WebGit import db
from flask_login.mixins import UserMixin
from WebGit.password_hash import *

ROLE_USER = 0
ROLE_ADMIN = 1

ACTIVE = 1
NOT_ACTIVE = 0


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(64), index = True)
    lastname = db.Column(db.String(64), index = True)
    nickname = db.Column(db.String(64), index = True, unique = True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    is_active = db.Column(db.SmallInteger, default = NOT_ACTIVE)
    repos = db.relationship('Repo', backref = 'owner', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Repo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.String(255));

    def __repr__(self):
        return '<Post %r>' % (self.body)