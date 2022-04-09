import requests
from flask import Blueprint, Response
from app.config import config as cfg
from src.data.connector import mongo_db

# added for the keyword based sort
import json
from src.Entities.Job import Job

hub_app = Blueprint("hub", __name__)


# @hub_app.route("/hub", methods=["GET"])
# def hub_jobs():
#     url = cfg.get("hub", "URL")
#     page = 1
#     while page < 25:
#         response = requests.get(f"{url}?page={page}").json()
#         jobs = response["docs"]
#         print(jobs)
#         mongo_db.push_jobs(jobs)
#     return Response(status=200, response={"success": True})


@hub_app.route("/hub", methods=["GET"])
def hub_jobs():

    search_cat = 'tech'
    page = 1
    pages = 2

    while page < pages:
        url = f'https://thehub.io/api/jobs?search={search_cat}+&page={page}'
        response = requests.get(url=url, headers={"Accept": "application/json"})
        pages = response.json()["pages"]
        des_jobs = Job.list_from_json(json.loads(response.content))
        mongo_db.push_jobs(des_jobs)
        print(f'Completed Page {page}, pushed {des_jobs.count} jobs')
        page += 1
    return Response(status=200, response={"success": True})
