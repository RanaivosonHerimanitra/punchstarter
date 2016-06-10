from punchstarter import db
from sqlalchemy.sql import func
import datetime
import cloudinary.utils

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
	image_filename = db.Column(db.String(200))
	time_start = db.Column(db.DateTime)
	time_ended = db.Column(db.DateTime)
	time_created = db.Column(db.DateTime)
	#a Project can have many pledges:
	pledges = db.relationship('Pledge',backref='project',foreign_keys='Pledge.project_id')

	@property
	def num_pledges(self):
		return len(self.pledges)
	@property
	def total_pledges(self):
		total_pledges=db.session.query( func.sum(Pledge.amount) ).filter(Pledge.project_id==self.id).one()[0]
		if total_pledges is None:
			total_pledges=0
		return total_pledges
	@property
	def num_days_left(self):
		now = datetime.datetime.now()
		num_days_left= (self.time_ended - now).days
		return num_days_left
	@property
	def image_path(self):
		return cloudinary.utils.cloudinary_url(self.image_filename)[0]


class Pledge (db.Model):
	id = db.Column(db.Integer,primary_key=True)
	member_id = db.Column(db.Integer,db.ForeignKey('member.id'),nullable=False)
	project_id = db.Column(db.Integer,db.ForeignKey('project.id'),nullable=False)
	amount =db.Column(db.Integer)
	time_created= db.Column(db.DateTime)
