from .db import db

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'genreID': self.id,
            'name': self.name
        }
