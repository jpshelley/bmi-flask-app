from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    bmi = db.Column(db.Integer)

    def __init__(self, height, weight, bmi):
        self.height = height
        self.weight = weight
        self.bmi = bmi

    def __repr__(self):
        return '<id {}>'.format(self.id)