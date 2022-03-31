from flask import Flask

from src.config import config as cfg

app = Flask(__name__)

app.config["SECRET_KEY"] = cfg.get("common", "SECRET_KEY")


debug = cfg.get("common", "DEBUG", fallback=False)
host = cfg.get("common", "HOST")
port = cfg.get("common", "PORT")
app.run(debug=debug, host=host, port=port)
