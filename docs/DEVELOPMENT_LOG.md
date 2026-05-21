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