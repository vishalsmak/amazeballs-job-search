import requests
import json
from src.Entities.Job import Job
from src.data.connector import mongo_db

search_cat = 'tech'
page = 1
pages = 2

while page < pages:
    url = f'https://thehub.io/api/jobs?search={search_cat}+&page={page}'
    response = requests.get(url=url, headers={"Accept":"application/json"})
    pages = response.json()["pages"]
    des_jobs = Job.list_from_json(json.loads(response.content))
    for job in des_jobs:
        mongo_db.push_jobs
    mongo_db.push_jobs(des_jobs)
    print(f'Completed Page {page}, pushed {des_jobs.count} jobs')
