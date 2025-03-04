from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variables
APP_ENV = os.getenv("APP_ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

