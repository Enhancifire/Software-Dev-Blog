def get_env():
    import os

    DB_URI = os.environ.get("MONGODB_URI")
    SECRET = os.environ.get("SECRET_KEY")

    return {
        "DB_URI": DB_URI,
        "SECRET_KEY": SECRET,
    }
