from flask import Flask
from app import db, ma

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	company = db.Column(db.String(50))
	email = db.Colummn(db.String(50))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	name = db.Column(db.String(50))
	phone = db.Column(db.String(20))
	picture = db.Column(db.String(50))

	skills = db.relationship("UserSkill")


class UserSkill(db.Model):
	__tablename__ = 'user_skills'
	id = db.Column(db.Integer, primary_key = True)
	rating = db.Column(Integer)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	

class Skill(db.Model):
	__tablename__ = 'skills'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(String(50))

	user_skills = db.relationship("UserSkill", backref="skills")



class UserSchema(ma.ModelSchema):
	class Meta:
		model = User

class UserSkillSchema(ma.ModelSchema):
	class Meta:
		model = UserSkill

class SkillSchema(ma.ModelSchema):
	class Meta:
		model = Skill


