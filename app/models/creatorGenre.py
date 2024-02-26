from .db import db

class CreatorGenre(db.Model):
    __tablename__ = 'creator_genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('creators.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    def to_dict(self):
        return {
            'creatorGenreID': self.id,
            'creatorID': self.creator_id,
            'genreID': self.genre_id
        }
