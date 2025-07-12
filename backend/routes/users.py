from fastapi import APIRouter
from backend.models import User
from backend.db.mongo import db

router = APIRouter()

@router.post("/")
def create_user(user: User):
    db["users"].insert_one(user.dict())
    return {"message": "User created"}
