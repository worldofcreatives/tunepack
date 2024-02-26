from .db import db

class CreatorType(db.Model):
    __tablename__ = 'creator_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('creators.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)

    def to_dict(self):
        return {
            'creatorTypeID': self.id,
            'creatorID': self.creator_id,
            'typeID': self.type_id
        }
