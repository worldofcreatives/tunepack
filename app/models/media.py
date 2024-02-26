from .db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM

class Media(db.Model):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    file = db.Column(db.String(500), nullable=False)
    file_type = db.Column(ENUM('mp3', 'wav', 'jpg', 'png', name='file_types'), nullable=True)
    file_size = db.Column(db.Integer, nullable=True)
    duration = db.Column(db.Integer, nullable=True)  # Nullable for non-audio/video files
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('media', lazy=True))

    def to_dict(self):
        return {
            'mediaId': self.id,
            'name': self.name,
            'file': self.file,
            'fileType': self.file_type,
            'fileSize': self.file_size,
            'duration': self.duration,
            'userId': self.user_id,
            'isActive': self.is_active,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
