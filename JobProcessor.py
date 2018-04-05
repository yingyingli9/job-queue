from threading import Thread
import time
from model import *
import requests

class JobProcessor(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
    	while True:
    		# fetch all jobs with status as 0
    		incompleted_jobs = Job.query.filter_by(status=0)
    		# request the url
    		for job in incompleted_jobs:
    			r = requests.get(url=job.url)


    		# store the html and request status in database
    		time.sleep(1)