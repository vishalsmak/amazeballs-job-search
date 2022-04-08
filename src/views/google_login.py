import json
import logging

from app.config import config as cfg
import requests


from flask import Blueprint, request, Response

auth_app = Blueprint("auth", __name__)


@auth_app.route("/google/get_url", methods=["GET"])
def get_url():
    try:
        url = cfg.get("oauth-verification", "URL")
        response = requests.get(
            "{}/oauth/google".format(url),
            {
                "redirect_uri": cfg.get("platform", "URL"),
                "client_id": cfg.get("oauth-google", "CLIENT_ID"),
            },
        )
        return Response(
            json.loads(response.content),
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        logging.error("GetUrl create {}".format(error))
        return Response(
            {"error": "Internal server error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@auth_app.route("/google/callback", methods=["GET"])
def callback():
    try:
        url = cfg.get("oauth-verification", "URL")
        code = request.data.get("code")
        user_type = request.data.get("state")[-1]
        response = json.loads(
            requests.get(
                "{}/oauth/google/callback".format(url),
                {
                    "code": code,
                    "redirect_uri": cfg.get("platform", "URL"),
                    "client_id": cfg.get("oauth-google", "CLIENT_ID"),
                    "client_secret": cfg.get(
                        "oauth-google", "CLIENT_SECRET"
                    ),
                },
            ).content
        )

        email = response["email"]
        first_name = response["given_name"]
        last_name = response["family_name"]
        attributes = {"google_data": response}
    except Exception as error:
        logging.error("CallBack create {}".format(error))
        return Response(
            {"error": "Internal server error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
