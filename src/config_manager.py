import json
import os
from src.logger import get_logger

logger = get_logger("config_manager")

CONFIG_PATH = "config/config.json"

DEFAULT_CONFIG = {
    "database": {
        "path": "data/internship_manager.db"
    },
    "logging": {
        "level": "DEBUG",
        "file": "logs/app.log",
        "max_size_mb": 5,
        "backup_count": 3
    },
    "export": {
        "default_format": "json",
        "output_folder": "data/"
    },
    "app": {
        "name": "Internship Manager",
        "version": "1.0.0",
        "items_per_page": 20
    }
}

class ConfigManager:
    # Class-level variables to track the singular instance and configuration storage
    _instance = None
    _config = None

    def __new__(cls):
        """Overrides object creation to enforce the Singleton Design Pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self):
        """Loads configuration from disk, falling back to defaults if the file is missing."""
        if not os.path.exists(CONFIG_PATH):
            logger.warning("Config file not found. Using default fallback system values.")
            self._config = DEFAULT_CONFIG
            return

        try:
            with open(CONFIG_PATH, "r") as file:
                self._config = json.load(file)
            logger.info(f"Configuration successfully loaded from {CONFIG_PATH}")
        except Exception as e:
            logger.error(f"Failed to decode config JSON file: {e}. Falling back to defaults.")
            self._config = DEFAULT_CONFIG

    def get(self, section, key, default=None):
        """Safely extracts a specific configuration setting without risk of crashing."""
        if self._config is None:
            self.load()
        section_data = self._config.get(section, {})
        return section_data.get(key, default)

    def get_database_path(self):
        return self.get("database", "path", "data/internship_manager.db")

    def get_log_file(self):
        return self.get("logging", "file", "logs/app.log")

    def get_log_level(self):
        return self.get("logging", "level", "DEBUG")

    def get_app_name(self):
        return self.get("app", "name", "Internship Manager")

    def get_app_version(self):
        return self.get("app", "version", "1.0.0")

    def get_output_folder(self):
        return self.get("export", "output_folder", "data/")

    def get_items_per_page(self):
        return self.get("app", "items_per_page", 20)

    def display_config(self):
        """Helper diagnostics routine to display active configurations cleanly."""
        print(f"\n=== Current Configuration ===")
        print(f"App Name:        {self.get_app_name()}")
        print(f"App Version:     {self.get_app_version()}")
        print(f"Database Path:   {self.get_database_path()}")
        print(f"Log File:        {self.get_log_file()}")
        print(f"Log Level:       {self.get_log_level()}")
        print(f"Output Folder:   {self.get_output_folder()}")
        print(f"Items Per Page:  {self.get_items_per_page()}")
        print("=" * 40)