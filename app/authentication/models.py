from datetime import datetime

from flask_login import UserMixin

from app import db, bcrypt
from app import login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)
    files = db.relationship('File', backref='author', lazy='dynamic')

    def check_password(self, password) -> bool:
        return bcrypt.check_password_hash(self.user_password, password)

    @classmethod
    def create_user(cls, user, email, password):
        user = cls(
            user_name=user,
            user_email=email,
            user_password=bcrypt.generate_password_hash(password).decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()
        return user



