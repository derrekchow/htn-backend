from flask_restful import Resource

class UserData(Resource):
	def get(self, user_id):
		if user_id is None:
			return()
		return()

	def put(self, user_id):
		return()