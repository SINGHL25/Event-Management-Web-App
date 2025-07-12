from fastapi import APIRouter, HTTPException
from backend.db.mongo import db
from backend.models import Event

router = APIRouter()

@router.get("/")
def get_events():
    return list(db["events"].find({}, {"_id": 0}))

@router.post("/")
def create_event(event: Event):
    db["events"].insert_one(event.dict())
    return {"message": "Event added successfully"}
