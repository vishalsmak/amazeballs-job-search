from urllib.parse import urlencode

import requests
from flask import Blueprint, Response, render_template, request

from app.config import config as cfg
from src.data.connector import mongo_db
from src.forms.search import SearchForm

google_app = Blueprint("google", __name__)
scope = "profile email openid"


def get_google_url():
    url = ""
    try:
        callback_url = f"{cfg.get('google', 'REDIRECT_URI')}/google/callback"
        data = {
            "response_type": "code",
            "client_id": cfg.get("google", "CLIENT_ID"),
            "redirect_uri": callback_url,
            "scope": scope,
            "access_type": "offline",
            "include_granted_scopes": "true",
        }
        querystring = urlencode(data)
        url = f"https://accounts.google.com/o/oauth2/v2/auth?{querystring}"
    except Exception as error:
        print("get_google_url {}".format(error))
    return url


@google_app.route("/google/callback", methods=["GET"])
def callback():
    print("Called by google!!")
    try:
        callback_url = f"{cfg.get('google', 'REDIRECT_URI')}/google/callback"
        response = requests.post(
            url="https://www.googleapis.com/oauth2/v4/token",
            data={
                "code": request.args.get("code"),
                "redirect_uri": callback_url,
                "client_id": cfg.get("google", "CLIENT_ID"),
                "client_secret": cfg.get("google", "CLIENT_SECRET"),
                "grant_type": "authorization_code",
            },
        ).json()

        response = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo?alt=json",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(response["access_token"]),
            },
        ).json()

        email = response["email"]
        first_name = response["given_name"]
        last_name = response["family_name"]
        attributes = {"google_data": response}
        user_name = f"{first_name} {last_name}"
        if not mongo_db.get_user(email):
            mongo_db.save_user(email, first_name, last_name, attributes)

        form = SearchForm()
        return render_template(
            "home.html", user_name=user_name, jobs={}, form=form
        )
    except Exception as error:
        print("callback {}".format(error))
        return Response(status=500)
