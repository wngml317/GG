from pybo import db

class Recycle(db.Model):
    item = db.Column(db.String(100), primary_key=True)
    division = db.Column(db.String(100), nullable=False)
    exhaust = db.Column(db.String(300), nullable=False)

