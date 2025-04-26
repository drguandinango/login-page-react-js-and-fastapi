import uvicorn
from fastapi import FastAPI, APIRouter
"""
from fastapi.middleware.cors import CORSMiddleware
from app.config import db
from app.service.auth_service import generate_role
"""
app = FastAPI()

router = APIRouter()

@router.get("/")
async def home():
        return "welcome home"

app.include_router(router)

def start():
        """Launched with 'poetry run start' at root level """
        uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)