from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "53070fbaabd54efe45ed035a467ecc3f"


if __name__ == "__main__":
    app.run(debug=True)
