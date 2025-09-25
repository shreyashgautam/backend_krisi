# app/services/soil_service.py
from app.database import soil_collection
from bson import ObjectId

# 1️⃣ Helper function to serialize MongoDB document
def serialize_doc(doc):
    """Convert MongoDB document to JSON-serializable dict"""
    doc["_id"] = str(doc["_id"])
    return doc

# 2️⃣ Insert soil data
def insert_soil_data(data: dict):
    soil_collection.insert_one(data)
    return {"message": "Data inserted successfully"}

# 3️⃣ Get latest soil data
def get_latest_soil_data():
    doc = soil_collection.find_one(sort=[("_id", -1)])
    if doc:
        return serialize_doc(doc)  # <-- apply serialization here
    return None

# 4️⃣ Get all soil data
def get_all_soil_data():
    docs = soil_collection.find()
    return [serialize_doc(d) for d in docs]  # <-- apply serialization here
