# streamlit_analytics.py
from pymongo import MongoClient
import pandas as pd
import streamlit as st

client = MongoClient("your-mongodb-uri")
events = list(client["eventhub"]["events"].find({}))
df = pd.DataFrame(events)

st.title("📊 Event Dashboard")
st.dataframe(df)

st.bar_chart(df['location'].value_counts())

