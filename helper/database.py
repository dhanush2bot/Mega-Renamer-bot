import pymongo
import os
from helper.date import add_date

DB_NAME = os.environ.get("DB_NAME", "DHANUSH")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://DHANUSH:DHANUSH@cluster0.2dppahj.mongodb.net/?retryWrites=true&w=majority")

mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]


def total_user():
    """
    Retrieves the total number of users in the database.

    Returns:
        int: The total number of users.
    """
    user = dbcol.count_documents({})
    return user


def botdata(chat_id):
    """
    Inserts bot data into the database.

    Args:
        chat_id (str): The chat ID.

    Returns:
        None
    """
    bot_id = int(chat_id)
    try:
        bot_data = {"_id": bot_id, "total_rename": 0, "total_size": 0}
        dbcol.insert_one(bot_data)
    except Exception as e:
        print(f"Error inserting bot data: {e}")


def total_rename(chat_id, renamed_file):
    """
    Updates the total rename count for a user.

    Args:
        chat_id (str): The chat ID.
        renamed_file (str): The current total rename count.

    Returns:
        None
    """
    now = int(renamed_file) + 1
    dbcol.update_one({"_id": chat_id}, {"$set": {"total_rename": str(now)}})


def total_size(chat_id, total_size, now_file_size):
    """
    Updates the total size for a user.

    Args:
        chat_id (str): The chat ID.
        total_size (str): The current total size.
        now_file_size (int): The size of the latest file.

    Returns:
        None
    """
    now = int(total_size) + now_file_size
    dbcol.update_one({"_id": chat_id}, {"$set": {"total_size": str(now)}})


def insert(chat_id):
    """
    Inserts user data into the database.

    Args:
        chat_id (str): The chat ID.

    Returns:
        bool: True if there was an error, else False.
    """
    user_id = int(chat_id)
    user_det = {"_id": user_id, "file_id": None, "caption": None, "daily": 0, "date": 0,
                "uploadlimit": 1288490188, "used_limit": 0, "usertype": "Free", "prexdate": None}
    try:
        dbcol.insert_one(user_det)
    except Exception as e:
        print(f"Error inserting user data: {e}")
        return True


def addthumb(chat_id, file_id):
    """
    Updates the file ID for a user's thumbnail.

    Args:
        chat_id (str): The chat ID.
        file_id (str): The file ID.

    Returns:
        None
    """
    dbcol.update_one({"_id": chat_id}, {"$set": {"file_id": file_id}})


def delthumb(chat_id):
    """
    Deletes the thumbnail for a user.

    Args:
        chat_id (str): The chat ID.

    Returns:
        None
    """
    dbcol.update_one({"_id": chat_id}, {"$set": {"file_id": None}})


def addcaption(chat_id, caption):
    dbcol.update_one({"_id": chat_id}, {"$set": {"caption": caption}})


def delcaption(chat_id):
    dbcol.update_one({"_id": chat_id}, {"$set": {"caption": None}})


def dateupdate(chat_id, date):
    dbcol.update_one({"_id": chat_id}, {"$set": {"date": date}})


def used_limit(chat_id, used):
    dbcol.update_one({"_id": chat_id}, {"$set": {"used_limit": used}})


def usertype(chat_id, type):
    dbcol.update_one({"_id": chat_id}, {"$set": {"usertype": type}})


def uploadlimit(chat_id, limit):
    dbcol.update_one({"_id": chat_id}, {"$set": {"uploadlimit": limit}})


def addpre(chat_id):
    date = add_date()
    dbcol.update_one({"_id": chat_id}, {"$set": {"prexdate": date[0]}})


def addpredata(chat_id):
    dbcol.update_one({"_id": chat_id}, {"$set": {"prexdate": None}})


def daily(chat_id, date):
    dbcol.update_one({"_id": chat_id}, {"$set": {"daily": date}})


def find(chat_id):
    id = {"_id": chat_id}
    x = dbcol.find(id)
    for i in x:
        file = i["file_id"]
        try:
            caption = i["caption"]
        except:
            caption = None

        return [file, caption]


def getid():
    values = []
    for key in dbcol.find():
        id = key["_id"]
        values.append((id))
    return values

def delete(id):
    dbcol.delete_one(id)


def find_one(id):
    """
    Finds a user by ID in the database.

    Args:
        id: The user ID.

    Returns:
        dict: User data if found, else None.
    """
    return dbcol.find_one({"_id": id})
