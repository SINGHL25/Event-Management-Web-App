from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import events, users

app = FastAPI()

# CORS (allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(events.router, prefix="/api/events", tags=["Events"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

# Static and Template
app.mount("/static", StaticFiles(directory="frontend/public"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/")
def read_root():
    return {"msg": "Welcome to EventHub API"}

