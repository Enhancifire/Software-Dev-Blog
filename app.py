from flask import Flask, redirect, render_template, request, flash, url_for
from vars import get_env
import database as db


app = Flask(__name__)

env = get_env()
app.config["SECRET_KEY"] = env["SECRET_KEY"]


@app.route("/")
def index():
    all_posts = db.get_all_posts()
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/featured")
def featured():
    return render_template("index.html")


@app.route("/deepdive")
def deepdive():
    posts = db.get_categorical_posts("Deep Dives")
    return render_template("index.html", posts=posts)


@app.route("/<post_id>")
def post(post_id):
    post = db.get_post(post_id)
    return render_template(
        "post.html",
        post=post,
    )


@app.route("/category/<cat>")
def get_categorical_posts(cat):
    posts = db.get_categorical_posts(cat)

    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
