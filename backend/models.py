```python
from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    title: str
    description: str
    location: str
    date: str
    created_by: str

class User(BaseModel):
    username: str
    email: str
    password: str
