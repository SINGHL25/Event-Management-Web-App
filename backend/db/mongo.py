from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
if not MONGO_URI:
    raise Exception("MongoDB URI not found")

client = MongoClient(MONGO_URI)
db = client["eventhub"]



