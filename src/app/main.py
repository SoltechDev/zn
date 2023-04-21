from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from db.register import register_tortoise
from db.config import TORTOISE_ORM
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

Tortoise.init_models(["db.models"], "models")
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
@app.get("/")
def home():
    return "Hello, World!"