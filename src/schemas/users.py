from tortoise.contrib.pydantic import pydantic_model_creator
from db.models import User

UserInSchema = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
UserOutSchema = pydantic_model_creator(User, name="UserOut", exclude=["password", "created_at", "updated_at"])
UserDatabaseSchema = pydantic_model_creator(User, name="User", exclude=["password", "created_at", "updated_at"])
