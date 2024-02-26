from .db import db
from datetime import datetime

class Opportunity(db.Model):
    __tablename__ = 'opportunities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_audience = db.Column(db.String(255), nullable=True)
    budget = db.Column(db.Numeric(10, 2), nullable=True)
    guidelines = db.Column(db.Text, nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    company = db.relationship('Company', backref=db.backref('opportunities', lazy=True))
    genres = db.relationship('Genre', secondary='opportunity_genres', backref=db.backref('opportunities', lazy='dynamic'))
    media = db.relationship('Media', secondary='opportunity_media', backref=db.backref('opportunities', lazy='dynamic'))


    def to_dict(self):
        return {
            'oppId': self.id,
            'name': self.name,
            'description': self.description,
            'targetAudience': self.target_audience,
            'budget': float(self.budget) if self.budget else None,
            'guidelines': self.guidelines,
            'companyId': self.company_id,
            'isActive': self.is_active,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
