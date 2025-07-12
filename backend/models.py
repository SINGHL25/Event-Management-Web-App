from pydantic import BaseModel

class Event(BaseModel):
    name: str
    category: str
    location: str

class User(BaseModel):
    username: str
    email: str
