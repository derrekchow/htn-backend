from app import app, api
from flask_restful import Api

from app.resources.users import Users
from app.resources.userSkills import UserSkills

api = Api(app)

api.add_resource(UserData, '/users/', '/users/<int:user_id>')
api.add_resource(UserSkills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)