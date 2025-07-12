import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))
events = list(client["eventhub"]["events"].find({}, {"_id": 0}))

st.set_page_config(page_title="EventHub Analytics", layout="wide")
st.title("📊 EventHub Analytics")

if not events:
    st.warning("No events found.")
else:
    st.dataframe(events)
    category_counts = {}
    for event in events:
        category = event.get("category", "Unknown")
        category_counts[category] = category_counts.get(category, 0) + 1

    st.bar_chart(category_counts)



