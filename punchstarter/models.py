from punchstarter import db

class Member (db.Model):
	id = db.Column(db.Integer,primary_key=True)
	first_name=db.Column(db.String(100))
	last_name=db.Column(db.String(100))
	project = db.relationship('Project',backref='creator')
	pledges = db.relationship('Pledge',backref='pledgor',foreign_keys='Pledge.member_id')
class Project (db.Model):
	id = db.Column(db.Integer,primary_key=True)
	member_id = db.Column(db.Integer,db.ForeignKey('member.id'),nullable=False)
	name=db.Column(db.String(100))
	short_description=db.Column(db.Text)
	long_description = db.Column(db.Text)
	goal_amount = db.Column(db.Integer)
	time_start = db.Column(db.DateTime)
	time_ended = db.Column(db.DateTime)
	time_created = db.Column(db.DateTime)
	#a Project can have many pledges:
	pledges = db.relationship('Pledge',backref='project',foreign_keys='Pledge.project_id')
class Pledge (db.Model):
	id = db.Column(db.Integer,primary_key=True)
	member_id = db.Column(db.Integer,db.ForeignKey('member.id'),nullable=False)
	project_id = db.Column(db.Integer,db.ForeignKey('project.id'),nullable=False)
	amount =db.Column(db.Integer)
	time_created= db.Column(db.DateTime)
