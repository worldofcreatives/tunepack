from .db import db
from datetime import datetime

class NotificationPreference(db.Model):
    __tablename__ = 'notification_preferences'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    notification_type = db.Column(db.String(255), nullable=False)  # Consider ENUM if supported
    enabled = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'preferenceID': self.id,
            'userID': self.user_id,
            'notificationType': self.notification_type,
            'enabled': self.enabled,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }
