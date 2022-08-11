from datetime import datetime
from app import db


class File(db.Model):
    __tablename__ = 'File'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(350))
    filename = db.Column(db.String(100))
    file = db.Column(db.PickleType)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH A RELATIONSHIP BETWEEN PUBLICATION AND BOOK TABLES
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, description, filename, file, user_id):
        self.description = description
        self.filename = filename
        self.file = file
        self.user_id = user_id

    def __repr__(self):
        return 'name of file is {} by {}'.format(self.filename, self.description)
