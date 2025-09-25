from pymongo import MongoClient
from .config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
soil_collection = db[COLLECTION_NAME]
