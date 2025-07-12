from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import users, events

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routes
app.include_router(users.router)
app.include_router(events.router)

@app.get("/")
def root():
    return {"msg": "Welcome to EventHub API"}

