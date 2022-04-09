import requests
from flask import Blueprint, Response

from app.config import config as cfg
from src.data.connector import mongo_db

hub_app = Blueprint("hub", __name__)


@hub_app.route("/hub", methods=["GET"])
def hub_jobs():
    print("Fetching jobs from hub")
    url = cfg.get("hub", "URL")
    page = 1
    while page <= 30:
        response = requests.get(f"{url}?page={page}").json()
        jobs = response["docs"]
        mongo_db.push_jobs(jobs)
        print(f"Finished pushing page: ${page}")
        page += 1
    return Response(status=200, response={"success": True})
