from .db import db
from datetime import datetime

class OpportunityMedia(db.Model):
    __tablename__ = 'opportunity_media'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    opp_id = db.Column(db.Integer, db.ForeignKey('opportunities.id'), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    opportunity = db.relationship('Opportunity', backref=db.backref('opportunity_media', lazy='dynamic'))
    media = db.relationship('Media', backref=db.backref('opportunity_media', lazy='dynamic'))

    def to_dict(self):
        return {
            'opportunityMediaID': self.id,
            'oppID': self.opp_id,
            'mediaID': self.media_id,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
