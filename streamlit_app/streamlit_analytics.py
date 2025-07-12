# streamlit_app.py

import streamlit as st
from db import events_collection

st.set_page_config(page_title="EventHub Dashboard", layout="wide")
st.title("📊 EventHub Analytics Dashboard")

# Load events from MongoDB
events = list(events_collection.find())

if not events:
    st.warning("No events found in the database.")
else:
    # Display raw data
    st.subheader("Raw Event Data")
    st.dataframe(events)

    # Simple chart by event type (you can enhance this later)
    st.subheader("Event Count by Category")
    category_counts = {}
    for event in events:
        category = event.get("category", "Unknown")
        category_counts[category] = category_counts.get(category, 0) + 1

    st.bar_chart(category_counts)

    # Add new event
    st.subheader("➕ Add New Event")
    with st.form("event_form"):
        name = st.text_input("Event Name")
        category = st.selectbox("Category", ["Conference", "Workshop", "Concert", "Meetup", "Other"])
        location = st.text_input("Location")
        submit = st.form_submit_button("Add Event")

        if submit:
            if name and location:
                new_event = {
                    "name": name,
                    "category": category,
                    "location": location
                }
                events_collection.insert_one(new_event)
                st.success(f"Event '{name}' added successfully! Refresh to see the update.")
            else:
                st.error("Please fill in all required fields.")


