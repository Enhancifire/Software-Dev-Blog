from flask import Flask, redirect, render_template, request, flash
from vars import get_test_env
from pymongo import MongoClient
from datetime import datetime


app = Flask(__name__)

env = get_test_env()
app.config["SECRET_KEY"] = env["SECRET_KEY"]
client = MongoClient(env['DB_URI'])
posts = client.get_database("Blog").get_collection("posts")


@app.route("/")
def index():
    all_posts = posts.find()
    my_posts = all_posts
    print(all_posts)
    return render_template("index.html", posts=all_posts)
    # return render_template("index.html", posts=all_posts,)


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
