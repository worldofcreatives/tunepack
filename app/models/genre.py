from .db import db

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    # Updated relationships to use CreatorGenre
    creators = db.relationship(
        'Creator',
        secondary='creator_genres',
        back_populates='genres'
    )

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
