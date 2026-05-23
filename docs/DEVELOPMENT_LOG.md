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