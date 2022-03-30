from api import db
from api.models.author import AuthorModel


class QuoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raiting = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey(AuthorModel.id))
    text = db.Column(db.String(255), unique=False)

    def __init__(self, author: AuthorModel, text: str, raiting=0):
        self.author_id = author.id
        self.text = text
        self.raiting = raiting
