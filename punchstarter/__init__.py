#where you store route, call db:
from flask import Flask, render_template,request,redirect,url_for,abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
import datetime
app = Flask(__name__)
app.config.from_object('punchstarter.default_settings')
manager=Manager(app)


db= SQLAlchemy(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

from punchstarter.models import *

@app.route("/")
def hello():
	#return "Hello world"
    return render_template('index.html')

@app.route("/projects/create",methods=['GET','POST'])
def create():
	if request.method=="GET":
		return render_template("create.html")

	if request.method=="POST":
		now = datetime.datetime.now()
		time_end= request.form.get("funding_end_date")
		time_end= datetime.datetime.strptime(time_end,"%Y-%m-%d")
		print time_end
		new_project = Project(
			member_id = 1,
			name = request.form.get("project_name"),
			short_description = request.form.get("short_description"),
			long_description = request.form.get("long_description"),
			goal_amount = request.form.get("funding_goal"),
			time_start = now,
			time_ended = time_end,
			time_created = now
			)
		db.session.add(new_project)
		db.session.commit()
		return redirect(url_for('project_detail',project_id=new_project.id))


@app.route("/visualization/d3/")
def viz():
	return render_template("d3.html")

@app.route("/projects/<int:project_id>/")
def project_detail(project_id):
	#a query to the table "Project"
	project = db.session.query(Project).get(project_id)
	if project is None:
		abort(404)
	return render_template("project_detail.html",project=project)

@app.route("/projects/<int:project_id>/pledge",methods=['GET','POST'])
def pledge(project_id):
	project=db.session.query(Project).get(project_id)
	if project is None:
		abort(404)
	if request.method=="GET":
		return render_template("pledge.html",project=project )
	if request.method=="POST":
		guest_pledgor = db.session.query(Member).filter_by(id=2).one()
		#handle the form submission:
		new_pledge =Pledge (member_id=guest_pledgor.id,project_id=project.id,amount=request.form.get("amount"),time_created=datetime.datetime.now())
		#actual insertion into the database (db)
		db.session.add(new_pledge)
		db.session.commit()
		return redirect(url_for("project_detail",project_id=project.id))
