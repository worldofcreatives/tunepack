from .db import db
from datetime import datetime

class SubmissionMedia(db.Model):
    __tablename__ = 'submission_media'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sub_id = db.Column(db.Integer, db.ForeignKey('submissions.id'), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    submission = db.relationship('Submission', backref=db.backref('submission_media', lazy=True))
    media = db.relationship('Media', backref=db.backref('submission_media', lazy=True))

    def to_dict(self):
        return {
            'subMediaID': self.id,
            'subID': self.sub_id,
            'mediaID': self.media_id,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
