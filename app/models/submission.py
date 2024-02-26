from .db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM

class Submission(db.Model):
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('creators.id'), nullable=False)
    opp_id = db.Column(db.Integer, db.ForeignKey('opportunities.id'), nullable=False)
    status = db.Column(ENUM('Pending', 'Accepted', 'Rejected', name='submission_statuses'), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    creator = db.relationship('Creator', backref=db.backref('submissions', lazy=True))
    opportunity = db.relationship('Opportunity', backref=db.backref('submissions', lazy=True))
    submission_media = db.relationship('SubmissionMedia', backref='submission', lazy='dynamic')
    feedback = db.relationship('Feedback', backref='submission', lazy='dynamic')


    def to_dict(self):
        return {
            'subId': self.id,
            'creatorId': self.creator_id,
            'oppId': self.opp_id,
            'status': self.status,
            'isActive': self.is_active,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
