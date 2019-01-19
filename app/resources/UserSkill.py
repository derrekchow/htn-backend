from flask_restful import Resource
from app import db
from app.Model import UserSkill, Skill, UserSkillSchema
from marshmallow import pprint
from flask import request

class UserSkillResource(Resource):
	def get(self):
		params = request.args
		frequency = params.get('frequency')
		rating = params.get('rating')
		result = []

		sql_rating = ""
		if rating is not None:
			sql_rating = "WHERE rating >= " + rating

		sql_freq = ""
		if frequency is not None:
			sql_freq = "HAVING count(*) >= " + frequency

		sql = "SELECT skill_id, ROUND(AVG(rating), 2), count(*) FROM user_skills " + sql_rating +  " GROUP BY skill_id " + sql_freq + ";"

		skill_data = db.session.execute(sql).fetchall()
		for skill in skill_data:
			skill_result = {
				"id": skill[0],
				"name": Skill.query.get(skill[0]).name,
				"average_rating": skill[1],
				"frequency": skill[2]
			}
			result.append(skill_result)

		return result
