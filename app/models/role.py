from .db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_type = db.Column(ENUM('Creator', 'Company', name='user_types'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'roleID': self.id,
            'roleName': self.role_name,
            'description': self.description,
            'userType': self.user_type,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }
