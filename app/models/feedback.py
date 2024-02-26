from .db import db
from datetime import datetime

class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submissions.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    submission = db.relationship('Submission', backref=db.backref('feedback', lazy=True))
    sender = db.relationship('User', foreign_keys=[sender_id])

    def to_dict(self):
        return {
            'feedbackId': self.id,
            'submissionID': self.submission_id,
            'senderId': self.sender_id,
            'message': self.message,
            'createdDate': self.created_date.isoformat()
        }
