"""Pydantic validation for loading .env variables for the FastAPI"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): 

    UP_BANK_API_KEY: str
    LLM_BASE_URL: str 
    LLM_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

    