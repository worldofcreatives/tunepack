from .db import db
from datetime import datetime

class ConsentLog(db.Model):
    __tablename__ = 'consent_logs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    consent_type = db.Column(db.String(255), nullable=False)
    consent_given = db.Column(db.Boolean, nullable=False, default=True)
    consent_withdrawn = db.Column(db.DateTime, nullable=True)
    details = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'consentID': self.id,
            'userID': self.user_id,
            'consentType': self.consent_type,
            'consentGiven': self.consent_given,
            'consentWithdrawn': self.consent_withdrawn.isoformat() if self.consent_withdrawn else None,
            'details': self.details,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }
