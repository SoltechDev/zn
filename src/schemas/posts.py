from typing import Optional
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from db.models import Note

PostInSchema = pydantic_model_creator(
    Note, name="NoteIn", exclude="author_id", exclude_readonly=True
)

PostOutSchema = pydantic_model_creator(
    Note, name="Note", exclude=["updated_at", "author.password", "author.created_at", "author.updated_at"]
)

class UpdatePost(BaseModel):
    title: Optional[str]
    content: Optional[str]