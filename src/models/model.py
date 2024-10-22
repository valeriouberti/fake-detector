# Pydantic model for the request body
from pydantic import BaseModel


class Article(BaseModel):
    text: str
