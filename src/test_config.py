from src.config_manager import ConfigManager

print("=== Testing Configuration Manager ===\n")

# Instantiate our ConfigManager
config = ConfigManager()
config.load()

print("--- Display all settings ---")
config.display_config()

print("\n--- Access individual settings ---")
print(f"Database path: {config.get_database_path()}")
print(f"Log file:      {config.get_log_file()}")
print(f"App name:      {config.get_app_name()}")
print(f"Version:       {config.get_app_version()}")
print(f"Items per page: {config.get_items_per_page()}")

print("\n--- Test Singleton pattern ---")
config1 = ConfigManager()
config2 = ConfigManager()
if config1 is config2:
    print("Singleton works! Both variables point to the same object.")
else:
    print("Something went wrong with Singleton!")

print("\n--- Test default value ---")
missing = config.get("app", "nonexistent_key", "this is the default")
print(f"Missing key returns: {missing}")

print("\n=== Configuration Test Complete ===")