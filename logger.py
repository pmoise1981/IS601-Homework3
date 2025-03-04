import logging
import os

# Configure logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("calculator.log"),  # Log to file
        logging.StreamHandler()  # Print logs to console
    ]
)

logger = logging.getLogger(__name__)

