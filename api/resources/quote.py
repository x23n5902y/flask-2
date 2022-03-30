from api import Resource, reqparse, db
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quote_schema, quotes_schema


class QuoteResource(Resource):
    def get(self, author_id, quote_id):
        author = AuthorModel.query.get(author_id)
        if quote_id is None:  # Если запрос приходит по url: /authors/<int:author_id>/quotes
            quotes = author.quotes.all()
            return quote_schema.dump([quote for quote in quotes]), 200  # Возвращаем все цитаты автора

        quote = QuoteModel.query.get(quote_id)
        if quote:
            return quote_schema.dump(quote), 200
        return {"Error": "Quote not found"}, 404

    def put(self, author_id, quote_id):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("raiting")
        new_data = parser.parse_args()
        author = AuthorModel.query.get(author_id)
        quote = QuoteModel.query.get(quote_id)
        quote.author = author
        quote.text = new_data["text"]
        quote.raiting = new_data["raiting"]
        db.session.commit()
        return quote_schema.dump(quote), 200

    def delete(self, author_id=None, quote_id=None):
        author = AuthorModel.query.get(author_id)
        quote = QuoteModel.query.get(quote_id)
        if author is None:
            return {"Error": f"Author with  id={author_id} not found"}, 404
        if quote is None:
            return {"Error": f"Quote with  id={quote_id} not found"}, 404
        db.session.delete(quote)
        db.session.commit()
        return f"Quote with id={quote_id} is deleted.", 200

    # raise NotImplemented("Метод не реализован")


class QuotesListResource(Resource):
    def get(self):
        quotes = QuoteModel.query.all()
        return quotes_schema.dump([quote for quote in quotes]), 200  # Возвращаем ВСЕ цитаты

    def post(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True)
        quote_data = parser.parse_args()
        # TODO: раскомментируйте строку ниже, чтобы посмотреть quote_data
        print(f"{quote_data=}")
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404

        quote = QuoteModel(author, quote_data["text"])
        db.session.add(quote)
        db.session.commit()
        return quote_schema.dump(quote), 201