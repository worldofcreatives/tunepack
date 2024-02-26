from .db import db
from datetime import datetime

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    logo = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('company', uselist=False))

    def to_dict(self):
        return {
            'companyId': self.id,
            'userId': self.user_id,
            'name': self.name,
            'companyName': self.company_name,
            'bio': self.bio,
            'logo': self.logo,
            'isActive': self.is_active,
            'createdDate': self.created_date.isoformat(),
            'updatedDate': self.updated_date.isoformat()
        }
