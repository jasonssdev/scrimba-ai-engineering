from pathlib import Path
from dotenv import load_dotenv
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

API_KEY_POLYGON = os.getenv("API_KEY_POLYGON")
API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
ENV = os.getenv("ENV", "development")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"