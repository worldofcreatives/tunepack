from .db import db
# from .creatorType import CreatorType

class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    creators = db.relationship('Creator', secondary='creator_types', backref=db.backref('types', lazy='subquery'))
    opportunities = db.relationship('Opportunity', secondary='opportunity_types', backref=db.backref('types', lazy='subquery'))

