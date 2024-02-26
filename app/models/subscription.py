# from .db import db
# from datetime import datetime

# class Subscription(db.Model):
#     __tablename__ = 'subscriptions'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
#     status = db.Column(db.String(50), nullable=False, default='Pending')
#     subscription_type = db.Column(db.String(50), nullable=False)
#     start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     end_date = db.Column(db.DateTime, nullable=True)
#     last_payment_date = db.Column(db.DateTime, nullable=True)
#     next_payment_due_date = db.Column(db.DateTime, nullable=True)
#     stripe_subscription_id = db.Column(db.String(255), nullable=False, unique=True)

#     user = db.relationship('User', backref=db.backref('subscriptions', lazy=True))

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'status': self.status,
#             'subscription_type': self.subscription_type,
#             'start_date': self.start_date.isoformat(),
#             'end_date': self.end_date.isoformat() if self.end_date else None,
#             'last_payment_date': self.last_payment_date.isoformat() if self.last_payment_date else None,
#             'next_payment_due_date': self.next_payment_due_date.isoformat() if self.next_payment_due_date else None,
#             'stripe_subscription_id': self.stripe_subscription_id
#         }
