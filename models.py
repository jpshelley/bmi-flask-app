from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __repr__(self):
        return '<id {}>'.format(self.id)