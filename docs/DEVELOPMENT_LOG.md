# Internship Manager - Development Log

## [2026-05-18] - Project Setup
- Created the initial project directory structure (`src`, `docs`, `config`, `data`, `logs`).
- Initialized Git repository and made the first commits.
- Configured VS Code environment.

## [2026-05-19] — Day 2: Python Basics Review & First Class
- Reviewed data structures by implementing a student dictionary and a list containing multiple student dictionaries.
- Created the core `Student` data model class with attributes for student ID, personal details, and academic program.
- Implemented custom methods `get_full_name()` and `to_dict()` within the `Student` class to handle encapsulation of data and formatting.
- Created a separate `test_student.py` script to test class instantiation and process a collection of records using a loop.
- Resolved a `ModuleNotFoundError` by utilizing standard root module execution (`python3 -m src.test_student`) to maintain a clean project architecture.

## [2026-05-21] — Day 3: Expanding Classes & Relationships
- Created a `Supervisor` data model class to capture academic supervisor information and department assignments.
- Developed an `Activity` class to serve as a central coordinator for managing internship or thesis properties.
- Implemented object-to-object relationships by passing complete `Student` and `Supervisor` object references into the `Activity` instance.
- Verified relational connections and custom formatting logic using a dedicated test script (`test_relationships.py`).

## [2026-05-22] — Day 4: Managing Collections of Objects

- Created `StudentManager` class to handle collections of Student objects.
- Implemented add, remove, search, and filter methods.
- Added duplicate ID validation before adding new students.
- Used list comprehensions for efficient searching and filtering.
- Separated management logic from the Student class itself.
- Verified all operations using a dedicated test script.

## [2026-05-23] — Day 5: File Storage with JSON
- Added `from_dict()` class method to Student for reconstructing objects from raw dictionary data.
- Implemented `save_to_json()` method in StudentManager to persist student records to a JSON file.
- Implemented `load_from_json()` method to reload saved student data back into the application.
- Added file existence validation checks before attempting to read inputs to prevent runtime crashes.
- Verified full serialization and deserialization lifecycle works correctly via `test_json.py`.

## [2026-05-26] — Day 6: CSV Import & Export
- Implemented `export_to_csv()` method to save student records into a CSV file readable by Excel.
- Implemented `import_from_csv()` method to load student records from an existing CSV file.
- Added type conversion for numeric fields during CSV import.
- Introduced pandas library for data summary and analysis.
- Implemented `show_summary_with_pandas()` to display student statistics grouped by program and enrollment year.
- Verified full export and import cycle works correctly.

## [2026-05-27] — Day 7: Incorporating Professor Feedback & Advanced Validation
- Created a `requirements.txt` file in the root directory specifying project dependencies (`pandas`).
- Expanded and restructured `README.md` to map out the directory tree, describe core entity responsibilities, and document demonstration scripts.
- Shifted internal definitions explicitly to label current framework checks as demonstration scripts rather than formal unit tests.
- Designed a comprehensive `.validate()` runtime architecture inside the `Student` class to check for empty strings, structural email formatting (`@`), and proper logical enrollment year boundaries (2000–2030).
- Hooked the validation execution layer into `StudentManager.add_student()` to prevent corrupted or duplicate elements from entering memory collections.
- Authored `src/test_validation.py` to ensure all invalid data vectors are caught and logged successfully.

## [2026-05-28] — Day 8: SQLite Database Integration
- Implemented a relative database layer inside `src/database.py` with dedicated relational handling modules.
- Formulated schemas creating three individual target tables (`students`, `supervisors`, `activities`).
- Embedded robust `FOREIGN KEY` structural constraints to link ongoing activity items directly to student and supervisor table elements.
- Engineered safe parameter boundaries for full operational CRUD tracking:
  - `initialize_database()` for setup safety checks.
  - `insert_student()` using try/except parameters to capture unique integrity constraints.
  - `get_all_students()` and `get_student_by_id()` for array mapping tracking.
  - `update_student()` and `delete_student()` handling runtime row operations.
  - `search_students()` utilizing wildcard keyword text strings.
- Applied parameterized execution queries with `?` protection filters to defend the operational logic against SQL Injection bugs.
- Validated complete local system mechanics utilizing the `src/test_database.py` entry pipeline.

## [2026-05-29] — Day 9: Logging System
- Engineered a centralized system logger inside `src/logger.py` with multi-handler routing.
- Configured a `StreamHandler` to push core operational tracking summaries directly to the terminal interface.
- Integrated a `RotatingFileHandler` configured to persist a persistent, deep-dive rolling history file up to 5MB at `logs/app.log`.
- Classified event severity across standardized levels (`DEBUG` for query filters, `INFO` for system success, `WARNING` for structural validation rejections, and `ERROR` for file operational missing handles).
- refactored `StudentManager` to map tracking entries comprehensively into memory arrays.
- Executed integration checks via `src/test_logger.py` validating active generation channels.

## [2026-05-30] — Day 10: Configuration Management
- Created a centralized configuration file at `config/config.json` to manage variable application boundaries (database, logging settings, export options, and app metadata).
- Developed `src/config_manager.py` implementing a robust `ConfigManager` parsing class.
- Enforced the Singleton Design Pattern to guarantee a single configuration access entity is shared across runtime system processes.
- Embedded a hardcoded `DEFAULT_CONFIG` dictionary structure to provide predictable fallback paths if disk configurations are missing or broken.
- Refactored property access by constructing explicit utility methods (`get_database_path()`, `get_log_file()`, etc.) to isolate raw dictionary keys.
- Validated setup mechanisms using the `src/test_config.py` verification scenario script.

## [2026-05-31] — Day 11: Command Line Interface
- Developed `src/cli.py` to provide a robust, interactive text-based console menu dashboard.
- Mapped all terminal operations directly to corresponding functions within `StudentManager`.
- Created a top-level execution file (`main.py`) to serve as the unified application entry point.
- Protected input fields with specialized `try/except` statements to trap invalid user inputs cleanly.
- Verified successful cross-module initialization, data collection handling, list retrieval rendering, file outputs, and safe exit routines.

## [2026-06-01] — Day 12: Notes, Links and Documents Relational Management
- Expanded the relational database schema by engineering three new sub-tables (`notes`, `links`, `documents`).
- Implemented One-to-Many relational linking mapping via custom `FOREIGN KEY` constraints tethered directly to the primary `student_id`.
- Designed robust transactional database CRUD query hooks featuring sequential data reads and localized record deletions.
- Automated data indexing features utilizing `AUTOINCREMENT` primary markers alongside runtime `datetime.date` capture objects.
- Successfully verified structural cascade behaviors and relational insertions using the `src/test_notes_links.py` diagnostic verification wrapper.