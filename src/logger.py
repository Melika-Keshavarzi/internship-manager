import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    try:
        from src.config_manager import ConfigManager
        config = ConfigManager()
        log_file = config.get_log_file()
        log_level = config.get_log_level()
    except Exception:
        log_file = "logs/app.log"
        log_level = "DEBUG"

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger