from pymongo import MongoClient
from config import DATABASE_URI, DATABASE_NAME

client = None
db = None
files_collection = None
users_collection = None

if DATABASE_URI:
    client = MongoClient(DATABASE_URI)
    db = client[DATABASE_NAME]
    files_collection = db["files"]
    users_collection = db["users"]

def add_file(file_id, file_name, message_id):
    if files_collection is None:
        raise RuntimeError("DATABASE_URI is not configured.")
    return files_collection.update_one(
        {"file_id": file_id},
        {"$set": {
            "file_id": file_id,
            "file_name": file_name,
            "message_id": message_id
        }},
        upsert=True
    )

def search_files(query, limit=10):
    if files_collection is None:
        return []
    return list(
        files_collection.find(
            {"file_name": {"$regex": query, "$options": "i"}}
        ).limit(limit)
    )
