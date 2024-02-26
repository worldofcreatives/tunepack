from .db import db
from datetime import datetime

class Favorites(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    opp_id = db.Column(db.Integer, db.ForeignKey('opportunities.id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('favorites', lazy=True))
    opportunity = db.relationship('Opportunity', backref=db.backref('favorited_by', lazy=True))

    def to_dict(self):
        return {
            'favoriteID': self.id,
            'userID': self.user_id,
            'oppID': self.opp_id,
            'createdDate': self.created_date.isoformat()
        }
