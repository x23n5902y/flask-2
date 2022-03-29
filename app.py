from api import api, app
from api.resources.quote import QuoteResource, QuotesListResource
from api.resources.author import AuthorResource, AuthorsListResource
from api.resources.user import UserResource, UsersListResource
from config import Config

api.add_resource(QuoteResource,
                 '/authors/<int:author_id>/quotes/<int:quote_id>'
                 )
api.add_resource(QuotesListResource,
                 '/quotes',
                 '/authors/<int:author_id>/quotes'
                 )  # <-- requests
api.add_resource(AuthorResource,
                 '/authors/<int:author_id>',
                 )
api.add_resource(AuthorsListResource,
                 '/authors'
                 )  # <-- requests
api.add_resource(UserResource,
                 '/users/<int:author_id>',
                 )
api.add_resource(UsersListResource,
                 '/users'
                 )  # <-- requests



if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
