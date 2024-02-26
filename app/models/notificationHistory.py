from .db import db
class NotificationHistory(db.Model):
    __tablename__ = 'notification_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)
    sent_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(255), nullable=False)  # Consider ENUM if supported

    def to_dict(self):
        return {
            'historyID': self.id,
            'notificationID': self.notification_id,
            'sentAt': self.sent_at.isoformat(),
            'status': self.status
        }
