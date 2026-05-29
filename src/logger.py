import logging
import os
from logging.handlers import RotatingFileHandler

LOG_FILE = "logs/app.log"

def get_logger(name):
    """
    Returns a configured logger instance with both file and console handlers.
    Ensures that the log directory exists prior to creating file handlers.
    """
    logger = logging.getLogger(name)

    # Prevent adding duplicate handlers if get_logger is called multiple times
    if logger.handlers:
        return logger

    # Capture everything from DEBUG level and above internally
    logger.setLevel(logging.DEBUG)

    # Standard professional log formatting structure
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Ensure logs directory exists safely
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # 1. File Handler: Saves all detailed history up to 5MB before rotating
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 2. Console Handler: Streams immediate clean info straight to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Attach handlers to the active tracking instance
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger