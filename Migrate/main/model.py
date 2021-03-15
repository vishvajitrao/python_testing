from main.config import db

class Books(db.Model):
    __tablename__ = 'Books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)