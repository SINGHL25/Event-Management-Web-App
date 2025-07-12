# streamlit_analytics.py
pip install pymongo python-dotenv

from pymongo import MongoClient
import pandas as pd
import streamlit as st

client = MongoClient("mongodb+srv://akhisingh1989:WelcomeASI2024%23%40@cluster0.tlxm8tv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
events = list(client["eventhub"]["events"].find({}))
df = pd.DataFrame(events)

st.title("📊 Event Dashboard")
st.dataframe(df)

st.bar_chart(df['location'].value_counts())

