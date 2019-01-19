from flask_restful import Resource
from app import db
from app.Model import User, UserSchema, UserSkill, UserSkillSchema, SkillSchema
from marshmallow import pprint
from flask import request
import json

def addUser(user):
	user_skills = []
	for skill in user.skills:
		user_skills.append({
			"name": skill.skill.name,
			"rating": skill.rating
		})
	user = UserSchema().dump(user).data
	user['skills'] = user_skills
	return user

class UserResource(Resource):
	def get(self, user_id=None):
		if user_id is None:
			users = User.query.all()
			result = []
			for user in users:
				result.append(addUser(user))
		else:
			result = addUser(User.query.get(user_id))
		return result

	def put(self, user_id):
		user = User.query.get(user_id)
		data = request.get_json(force=True)
		valid_fields = ['id', 'company', 'email', 'latitude', 'longitude', 'name', 'phone', 'pictures']

		for key in data:
			if key in valid_fields:
				setattr(user, key, data[key])
			elif key == 'skills':
				skills_dict = dict()
				skills_arr = []
				for skill in data[key]:
					skills_dict[skill['name']] = skill['rating']
					skills_arr.append(skill['name'])

				for skill in user.skills:
					if skill.skill.name in skills_arr:
						skill.rating = skills_dict[skill.skill.name]
					else:
						print(skill)

		db.session.commit()
		
		# for skill in _:
		# 	skills = Skill.query.filter(Skill.name==).first()
		# 	skills = Skill(name=skills.name)
		# 	user_skill = UserSkill.queary.filter(user_id, skill_id)
		# 	if user_skill:
		# 		user_skill.name= 
		# 	else:
		# 		user_skill = UserSkill()
		# 		db.session.add(user_skill)

		# TODO: add a try except