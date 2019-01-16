from app import app, api
from flask_restful import Api

from app.resources.User import UsersResource
from app.resources.UserSkill import UserSkillResource

api = Api(app)

api.add_resource(UserResource, '/users/', '/users/<int:user_id>')
api.add_resource(UserSkillResource, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)