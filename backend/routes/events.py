from fastapi import APIRouter, HTTPException
from backend.db.mongo import db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/events", tags=["Events"])

class Event(BaseModel):
    title: str
    description: str
    date: datetime
    location: str
    created_by: str

@router.post("/")
def create_event(event: Event):
    db.events.insert_one(event.dict())
    return {"msg": "Event created!"}

@router.get("/")
def list_events():
    events = list(db.events.find({}, {"_id": 0}))
    return events

