import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.environ.get('OPENAI_API_KEY', '')


settings = Settings()