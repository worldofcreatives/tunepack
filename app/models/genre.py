from .db import db

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    # Relationship with Creators through CreatorGenre
    creators = db.relationship(
        'Creator',
        secondary='creator_genres',
        backref=db.backref('genres', lazy='dynamic')
    )

    # Relationship with Opportunities through OpportunityGenre
    opportunities = db.relationship(
        'Opportunity',
        secondary='opportunity_genres',
        backref=db.backref('genres', lazy='dynamic')
    )

    def to_dict(self):
        return {
            'genreID': self.id,
            'name': self.name
        }
