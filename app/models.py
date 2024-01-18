from app import db
from datetime import datetime

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(256))
    author = db.Column(db.String(128))
    published_date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Game {self.name}>'
