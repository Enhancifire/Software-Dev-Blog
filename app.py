from flask import Flask, redirect, render_template, request, flash
from vars import get_env

app = Flask(__name__)

env = get_env()
app.config["SECRET_KEY"] = env["SECRET_KEY"]


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
