from app.config import config as cfg
from src.data.connector import mongo_db
import requests

from flask import Blueprint, Response

hub_app = Blueprint("hub", __name__)


@hub_app.route("/hub", methods=["GET"])
def hub_jobs():
    url = cfg.get('hub', 'URL')
    page = 1
    while page < 25:
        response = requests.get(f'{url}?page={page}').json()
        jobs = response['docs']
        print(jobs)
        mongo_db.push_jobs(jobs)
    return Response(status=200, response={
        'success': True
    })
