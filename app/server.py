from flask import Flask
from flask_cors import CORS

from app.config import config as cfg
from src.data.hub import hub_app
from src.views.auth import auth_app
from src.views.google_login import google_app

app = Flask(
    __name__, template_folder="../templates", static_folder="../static"
)

app.config["SECRET_KEY"] = cfg.get("common", "SECRET_KEY")

if cfg.get("flask", "DEBUG", fallback=False):
    print("CORS enabled for the app !!")
    CORS(app)

# register blueprints
app.register_blueprint(auth_app)
app.register_blueprint(hub_app)
app.register_blueprint(google_app)


@app.route("/health_check", methods=["GET"])
def verify():
    return "Hurray!! Happy that I am alive. Have a good day :)"


if __name__ == "__main__":
    DEBUG = bool(cfg.get("common", "DEBUG", fallback=False))
    app.run(host="0.0.0.0", debug=DEBUG)
