from api import Resource, reqparse, db
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


# GET /authors/1 - author by id
class UserResource(Resource):
    def get(self, user_id):
        # Если запрос приходит по url: /authors/<int:author_id>
        user = UserModel.query.get(user_id)
        if user:
            return user_schema.dump(user), 200
        return f"Author id={user_id} not found", 404

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel.query.get(user_id)
        if user is None:
            return {"Error": f"Author id={user_id} not found"}, 404
        user.username = user_data["username"]
        user.password = user_data["password"]
        db.session.commit()
        return user_schema.dump(user), 200

    def delete(self, quote_id):

        raise NotImplemented("Метод не реализован")


# GET /authors - authors list
class UsersListResource(Resource):
    def get(self):
        users = UserModel.query.all()
        users_list = [user for user in users]
        return users_schema.dump(users_list), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201
