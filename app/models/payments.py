# from .db import db
# from datetime import datetime

# class Payment(db.Model):
#     __tablename__ = 'payments'

#     id = db.Column(db.Integer, primary_key=True)
#     subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'), nullable=False)
#     amount = db.Column(db.Numeric(10, 2), nullable=False)
#     payment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     stripe_payment_id = db.Column(db.String(255), nullable=False, unique=True)
#     status = db.Column(db.String(50), nullable=False)

#     subscription = db.relationship('Subscription', backref=db.backref('payments', lazy=True))

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'subscription_id': self.subscription_id,
#             'amount': float(self.amount),
#             'payment_date': self.payment_date.isoformat(),
#             'stripe_payment_id': self.stripe_payment_id,
#             'status': self.status
#         }
