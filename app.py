from flask import Flask, redirect, render_template, request, flash
from vars import get_env
from pymongo import MongoClient


app = Flask(__name__)

env = get_env()
app.config["SECRET_KEY"] = env["SECRET_KEY"]
client = MongoClient(env['DB_URI'])
posts = client.get_database("Blog").get_collection("posts")


@app.route("/")
def index():
    all_posts = posts.find()
    return render_template("index.html", posts=all_posts,)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/featured')
def featured():
    return render_template("index.html")


@app.route('/deepdive')
def deepdive():
    return render_template("index.html")


@app.route('/{id}')
def post(id):
    post = posts.find_one({"_id": id})
    return render_template("post.html", post=post,)


if __name__ == "__main__":
    app.run(debug=True)
