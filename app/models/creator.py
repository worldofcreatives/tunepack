from .db import db
from datetime import datetime

class Creator(db.Model):
    __tablename__ = 'creators'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('Producer', 'Writer', 'Musician'), nullable=False)
    genres = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('creator', uselist=False))

    def to_dict(self):
        return {
            'creatorId': self.id,
            'userId': self.user_id,
            'name': self.name,
            'type': self.type,
            'genres': self.genres,
            'status': self.status,
            'profilePic': self.profile_pic,
            'isActive': self.is_active,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
