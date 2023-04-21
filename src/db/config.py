import os
from dotenv import load_dotenv

load_dotenv()
if not os.environ.get("DATABASE_URL"):
    raise Exception("Error env variable DATABASE_URL not found")
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "db.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}