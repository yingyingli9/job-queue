from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# model definitions

class Job(db.Model):
	"""Information of a particular job."""

	__tablename__ = "jobs"


	job_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	url = db.Column(db.String(500), nullable=False)
	# True = Completed
	status = db.Column(db.Boolean, nullable=False)

class Response(db.Model):
	"""Contents of the response divided into parts of 1000 characters."""

	__tablename__ = "responses"

	response_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	content = db.Column(db.String(1000), nullable=False)
	job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)

	# create a relationship between response and job tables
	job = db.relationship("Job", backref = 'responses')