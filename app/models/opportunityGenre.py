from .db import db

class OpportunityGenre(db.Model):
    __tablename__ = 'opportunity_genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    opportunity_id = db.Column(db.Integer, db.ForeignKey('opportunities.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    def to_dict(self):
        return {
            'opportunityGenreID': self.id,
            'opportunityID': self.opportunity_id,
            'genreID': self.genre_id
        }
