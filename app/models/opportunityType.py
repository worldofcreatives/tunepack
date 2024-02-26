from .db import db

class OpportunityType(db.Model):
    __tablename__ = 'opportunity_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    opportunity_id = db.Column(db.Integer, db.ForeignKey('opportunities.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)

    def to_dict(self):
        return {
            'opportunityTypeID': self.id,
            'opportunityID': self.opportunity_id,
            'typeID': self.type_id
        }
