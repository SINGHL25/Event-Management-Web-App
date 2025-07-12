from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URI", "your-mongodb-uri")
client = MongoClient(MONGO_URL)
db = client["eventhub"]

