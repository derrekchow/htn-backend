from flask_restful import Resource
from Model import UserSkill, UserSkillResource

class UserSkillResource(Resource):
	def get(self):
		return()