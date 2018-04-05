from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

from flask import (Flask, render_template, redirect, request,
                   session, jsonify)

from model import *
from jobProcessor import *


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route("/")
def display_jobs():
	"""Display jobs that the user added ordered chronologically."""
	jobs = Job.query.all()

	return render_template("jobs.html", jobs = jobs)

@app.route("/add_job", methods=["POST"])
def add_job():
	"""Add job to the queue."""
	url = request.form.get("url")
	new_job = Job(url=url, status=0)
	db.session.add(new_job)
	db.session.commit()

	# send it as AJAX request with status as not completed

	# payloads = {"job_id": new_job.job_id, "url": new_job.url}

	# return jsonify(payloads)

	return redirect("/")

@app.route("/get_status", methods=["POST"])
def get_status():
	"""Display the status of a certain job."""
	job_id = request.form.get("job_id")
	job = Job.query.get(int(job_id))
	if job.status == 1:
		# contents = Response.query.filter_by(job_id=job_id)
		# html_content = "".join(contents)
		status = "Completed"
	if job.status == 0:
		status = "Not Completed"
	if job.status == -1:
		status = "Invalid"
		# content = None
	return jsonify({'job_status': status, "job_id": job_id})

@app.route("/get_response", methods=["POST"])
def get_response():
	"""Open a new page that displays response as HTML of a certain job."""
	job_id = request.form.get("job_id")
	# handle invalid case
	responses = Response.query.filter_by(job_id=job_id).all()
	html_content = ""
	for response in responses:
		html_content += response.content
	return jsonify({"job_id": job_id, "response": html_content})








if __name__ == "__main__":

	# Create job processor
	# jobProcessor = JobProcessor()
	# jobProcessor.start()
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True
    # make sure templates, etc. are not cached in debug mode
	app.jinja_env.auto_reload = app.debug

	connect_to_db(app)
	db.create_all()

    # Use the DebugToolbar
	DebugToolbarExtension(app)

	app.run(port=5000, host='0.0.0.0')




