from .db import db

class FeedbackMedia(db.Model):
    __tablename__ = 'feedback_media'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable=False)

    feedback = db.relationship('Feedback', backref=db.backref('feedback_media', lazy=True))
    media = db.relationship('Media', backref=db.backref('feedback_media', lazy=True))

    def to_dict(self):
        return {
            'feedbackMediaId': self.id,
            'feedbackId': self.feedback_id,
            'mediaId': self.media_id
        }
