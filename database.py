from vars import get_env
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo
from datetime import datetime


def create_connection():
    """Creates connection to the database"""
    env = get_env()
    client = MongoClient(env["DB_URI"])

    posts = client.get_database("Blog").get_collection("posts")

    return posts


def convert_date(date):
    """Converts date from ISO Format to 'M D, YYYY' Format"""

    return datetime.fromisoformat(date).strftime("%B %d, %Y")


def get_all_posts():
    """Retrieves a list of latest 10 posts"""
    POSTS = create_connection()
    my_posts = list(POSTS.find().limit(10).sort("date", pymongo.DESCENDING))
    for post in my_posts:
        post["date"] = convert_date(post["date"])

    return my_posts


def get_post(_id):
    """Retrieve a post based on the id as parameter"""

    POSTS = create_connection()
    post = POSTS.find_one({"_id": ObjectId(_id)})

    post["date"] = convert_date(post["date"])

    return post


def get_categorical_posts(category):
    """Retrieves posts based on the category"""

    POSTS = create_connection()
    posts = list(POSTS.find({"categories": category}))
    for post in posts:
        post["date"] = convert_date(post["date"])

    return posts
