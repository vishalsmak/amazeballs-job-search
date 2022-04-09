# added for the keyword based sort
import json

import requests
from flask import Blueprint, Response, request

from app.config import config as cfg
from src.data.connector import mongo_db
from src.entities.job import Job

hub_app = Blueprint("hub", __name__)


@hub_app.route("/hub", methods=["GET"])
def hub_jobs():
    url = cfg.get("hub", "URL")
    search_cat = "tech"
    page = 1
    pages = 2

    while page < pages:
        url = f"{url}?search={search_cat}+&page={page}"
        response = requests.get(
            url=url, headers={"Accept": "application/json"}
        )
        pages = response.json()["pages"]
        des_jobs = Job.list_from_hub_json(json.loads(response.content))
        mongo_db.push_jobs(des_jobs)
        print(f"Completed Page {page}, pushed {des_jobs.count} jobs")
    return Response(status=200, response={"success": True})


@hub_app.route("/getJobs", methods=["POST"])
def get_jobs_keywords():
    job_list = []
    for job in mongo_db.get_jobs(request.get_json()["keywords"]):
        job_list.append(job)
    print(job_list)
    return Response(
        status=200,
        response=json.dumps(job_list),
        headers={"Content-Type": "application/json"},
    )
