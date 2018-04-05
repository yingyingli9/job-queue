from flask_sqlalchemy import SQLAlchemy
# import enum

db = SQLAlchemy()


# class Status(enum.Enum):
# 	completed = 1
# 	not_completed = 0
# 	invalid = -1

# model definitions

class Job(db.Model):
	"""Information of a particular job."""

	__tablename__ = "jobs"


	job_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	url = db.Column(db.String(500), nullable=False)
	# True = Completed

	# Change type as a integer. The value will be a enum value.
	# completed = 1
	# not_completed = 0
	# invalid = -1
	status = db.Column(db.Integer, nullable=False)



class Response(db.Model):
	"""Contents of the response divided into parts of 1000 characters."""

	__tablename__ = "responses"

	response_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	content = db.Column(db.String(1000), nullable=False)
	job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)

	# create a relationship between response and job tables
	job = db.relationship("Job", backref = 'responses')


def connect_to_db(app, link='postgresql:///job-queue'):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = link
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
