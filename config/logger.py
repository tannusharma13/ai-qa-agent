import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("AI_QA_COPILOT")
logger.setLevel(logging.INFO)

# Prevent duplicate logs if imported multiple times
if not logger.handlers:

    # File handler
    file_handler = logging.FileHandler(
        "logs/pipeline.log",
        mode="a",
        encoding="utf-8"
    )

    # Console handler
    console_handler = logging.StreamHandler()

    # Common log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)