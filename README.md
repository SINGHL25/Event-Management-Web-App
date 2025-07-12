# Event-Management-Web-App
🎟️ Build a personal Event Management Web App Like Eventbrite: Users can browse, register, and host events, with full admin, dashboard, bookings, location, and filtering support.
# eventhub-app/README.md

# 🌟 EventHub - Event Management Web App

EventHub is a Python-based full-stack event management platform similar to Eventbrite. Users can browse, create, and manage events. Built using FastAPI (backend), MongoDB Atlas (database), and simple HTML/JS or React (frontend).

---

## 🚀 Features
- User can create events
- Events have title, description, date, location, creator
- Store data in MongoDB (free tier)
- Clean, minimal dashboard
- Responsive frontend (HTML+JS or React)
- FastAPI backend RESTful API

---

## 🚫 Future Scope
- User authentication
- Event booking
- Admin dashboard
- Email notifications
- Android app (Flutter/React Native)

---

## 📂 Project Structure

```
eventhub-app/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   │   ├── users.py
│   │   └── events.py
│   ├── db/
│   │   └── mongo.py
│   └── utils/
├── frontend/
│   ├── public/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   └── app.js
├── requirements.txt
├── .env
└── README.md
```
