from app import db
from app.Model import User, UserSkill, Skill
from marshmallow import pprint
import json

with open('data/users.json') as file:
    data = json.load(file)

db.create_all()

for user in data:
	user_model = User(
		company=user['company'],
		email=user['email'],
		name=user['name'],
		latitude=user['latitude'],
		longitude=user['longitude'],
		phone=user['phone'],
		picture=user['picture']
		)
	db.session.add(user_model)
	db.session.flush()
	print("\nAdded user '" + user_model.name + "'")

	for skill in user['skills']:
		if Skill.query.filter(Skill.name == skill['name']).first() is None:
			skill_model = Skill( name=skill['name'] )
			db.session.add(skill_model)
			db.session.flush()
		else:
			skill_model = Skill.query.filter(Skill.name == skill['name']).first()

		user_skill_model = UserSkill(
			rating=skill['rating'],
			user_id=user_model.id,
			skill_id=skill_model.id
		)
		print("\tAdded skill '" + skill_model.name + "'")
		db.session.add(user_skill_model)

db.session.commit()