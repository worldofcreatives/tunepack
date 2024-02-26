
from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
import os
import binascii

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(255), nullable=False)  # Store the salt
    type = db.Column(db.Enum('Creator', 'Company'), default='Creator', nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='target_user', lazy=True)
    notification_preferences = db.relationship('NotificationPreference', backref='user', lazy=True)
    consent_logs = db.relationship('ConsentLog', backref='user', lazy=True)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.salt = binascii.hexlify(os.urandom(16)).decode()  # Generate a new salt
        # Incorporate the salt with the password before hashing
        self.hashed_password = generate_password_hash(password + self.salt)

    def check_password(self, password):
        # Use the salt from the database with the input password to check against the hashed password
        return check_password_hash(self.hashed_password, password + self.salt)

    def to_dict(self):
        return {
            'userId': self.id,
            'username': self.username,
            'email': self.email,
            'type': self.type,
            'createdDate': self.createdDate.isoformat(),
            'updatedDate': self.updatedDate.isoformat(),
        }
