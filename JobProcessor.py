from threading import Thread
import time
from model import *
import requests
import re

class JobProcessor(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while True:
		# fetch all jobs with status as 0
			incompleted_jobs = Job.query.filter_by(status=0).all()
			# print("size: " + str(len(incompleted_jobs)))
			# request the url
			for job in incompleted_jobs:
				job.status = -2
				db.session.commit()
				if job.url[:4] != 'http':
					url = 'http://' + job.url
				else:
					url = job.url
				try:
					r = requests.get(url=url)

				except requests.ConnectionError: 
					job.status = -1
					db.session.commit()
					continue


				if r.status_code == 200:
					# store the html and request status in database
					# divide the html text into parts of 10000 characters
					parts = map(''.join, zip(*[iter(r.text)]*1000))
					extra = r.text[len(parts) * 1000:]
					if extra:
						parts.append(extra)
					for part in parts:
						response = Response(content=part, job_id=job.job_id)
						db.session.add(response)
						db.session.commit()

					job.status = 1
					db.session.commit()
					print job.status
				else:
					job.status = -1
					db.session.commit()
					# print "I should not be here."
			time.sleep(5)

