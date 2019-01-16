from flask_restful import Resource
from Model import User, UserSchema

class UserResource(Resource):
	def get(self, user_id):
		if user_id is None:
			return()
		return()

	def put(self, user_id):
		return()