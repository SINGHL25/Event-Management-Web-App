from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI=mongodb+srv://akhisingh1989:WelcomeASI2024%23%40@cluster0.tlxm8tv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

if not MONGO_URI:
    raise Exception("❌ MongoDB URI not set in .env file")

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client["eventhub"]  # Database name
events_collection = db["events"]  # Collection name

# Optional: test connection
try:
    client.admin.command('ping')
    print("✅ MongoDB connection successful")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

