def get_env():
    import os

    DB_URI = os.environ.get("MONGODB_URI")
    SECRET = os.environ.get("SECRET_KEY")

    return {
        "DB_URI": DB_URI,
        "SECRET_KEY": SECRET,
    }

def get_test_env():

    from test import SECRET, DB_URI

    return {
        "DB_URI": DB_URI,
        "SECRET_KEY": SECRET,
    }
    