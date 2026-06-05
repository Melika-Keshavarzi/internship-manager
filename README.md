# Internship Manager

A Python-based management system for organizing and monitoring
internships and thesis activities in an academic environment.

## Project Description

This application supports the organization and monitoring of
interns and thesis students involved in academic and research
activities. It is built using object-oriented Python and follows
a modular architecture with clear separation between data classes,
management logic, persistence, and user interaction.

This project was developed as part of an academic software
engineering exercise under the supervision of
Professor Francesco La Rosa, University of Messina.

## Project Structure

internship-manager/
├── src/
│   ├── __init__.py             Package initialization
│   ├── student.py              Student data class with validation
│   ├── supervisor.py           Supervisor data class
│   ├── activity.py             Activity data class (internship/thesis)
│   ├── student_manager.py      Collection management and file I/O
│   ├── database.py             SQLite database layer (all CRUD operations)
│   ├── logger.py               Centralized logging configuration
│   ├── config_manager.py       Configuration management (Singleton)
│   ├── cli.py                  Interactive command-line interface
│   ├── report_generator.py     Progress report generation
│   ├── test_student.py         Demonstration script for Student class
│   ├── test_relationships.py   Demonstration script for class relationships
│   ├── test_manager.py         Demonstration script for StudentManager
│   ├── test_json.py            Demonstration script for JSON persistence
│   ├── test_csv.py             Demonstration script for CSV import/export
│   ├── test_validation.py      Demonstration script for data validation
│   ├── test_database.py        Demonstration script for SQLite database
│   ├── test_logger.py          Demonstration script for logging system
│   ├── test_config.py          Demonstration script for ConfigManager
│   ├── test_notes_links.py     Demonstration script for notes and links
│   └── test_reports.py         Demonstration script for activity reports
├── data/
│   ├── students.json           JSON export file
│   ├── students.csv            CSV export file
│   └── internship_manager.db   SQLite database file
├── config/
│   └── config.json             Application configuration file
├── logs/
│   └── app.log                 Application log file
├── docs/
│   └── DEVELOPMENT_LOG.md      Daily development log
├── requirements.txt            Project dependencies
├── main.py                     Main application entry point
├── README.md                   Project documentation
└── .gitignore                  Git ignore rules

## Main Classes and Modules

### Student (src/student.py)
Represents a student with personal and academic information.
Attributes: student_id, first_name, last_name, email, phone,
enrollment_year, degree_program.
Methods: get_full_name(), to_dict(), from_dict(), validate()
The validate() method checks for empty fields, valid email
format, and valid enrollment year range (2000-2030).

### Supervisor (src/supervisor.py)
Represents an academic supervisor.
Attributes: supervisor_id, first_name, last_name, email, department.

### Activity (src/activity.py)
Represents an internship or thesis activity.
Links a Student object and a Supervisor object together.
Attributes: activity_id, activity_type, title, topic,
start_date, end_date, status, student, supervisor.
Activity types: internship, thesis.
Activity statuses: active, pending, completed.

### StudentManager (src/student_manager.py)
Handles collections of Student objects in memory.
Provides methods for adding, removing, searching, filtering,
and persisting student data to JSON and CSV files.
Note: This class manages in-memory collections.
For permanent storage, the SQLite database layer is used.

### Database (src/database.py)
SQLite database layer for permanent data storage.
Contains functions for full CRUD operations on:
- students table
- supervisors table
- activities table
- notes table
- links table
- documents table
This is the main persistence mechanism of the application.
JSON and CSV are used as import/export features only.

### Logger (src/logger.py)
Centralized logging configuration using Python logging library.
Writes logs to both the terminal and logs/app.log file.
Uses RotatingFileHandler to manage log file size automatically.
Log levels used:
- DEBUG: detailed search and query operations
- INFO: successful operations
- WARNING: validation failures and duplicates
- ERROR: missing files and failed operations

### ConfigManager (src/config_manager.py)
Reads and applies settings from config/config.json.
Implements the Singleton design pattern.
Provides fallback default values if config file is missing.
All modules read their paths and settings from this class.
Settings managed: database path, log file, log level,
export folder, app name, version, items per page.

### CLI (src/cli.py)
Interactive command-line interface for the application.
Provides a full menu-driven system for all student operations.
Completely separated from business logic.
Handles input validation and user confirmation prompts.

### ReportGenerator (src/report_generator.py)
Generates progress reports for the application.
generate_full_report() produces:
- Total students registered
- Activity summary by status
- Upcoming deadlines within 30 days
- Activities grouped by type
generate_student_report() produces:
- Full personal information
- All notes with dates
- All links with types and descriptions
- All documents with upload dates

### main.py
Single entry point for the application.
Run this file to start the interactive CLI.

## Database Schema

The SQLite database contains 6 tables:

students:
  student_id (PRIMARY KEY), first_name, last_name,
  email, phone, enrollment_year, degree_program

supervisors:
  supervisor_id (PRIMARY KEY), first_name, last_name,
  email, department

activities:
  activity_id (PRIMARY KEY), activity_type, title, topic,
  start_date, end_date, status,
  student_id (FOREIGN KEY), supervisor_id (FOREIGN KEY)

notes:
  note_id (PRIMARY KEY AUTOINCREMENT),
  student_id (FOREIGN KEY), date, content

links:
  link_id (PRIMARY KEY AUTOINCREMENT),
  student_id (FOREIGN KEY), link_type, url, description

documents:
  doc_id (PRIMARY KEY AUTOINCREMENT),
  student_id (FOREIGN KEY), file_path, description, upload_date

## Storage Mechanisms

This project uses three storage mechanisms with distinct purposes:

SQLite Database (data/internship_manager.db)
This is the MAIN and PRIMARY persistence mechanism.
All student records, notes, links, documents, supervisors,
and activities are permanently stored here.
Data survives between program runs through the database.

JSON Files (data/students.json)
Used as an import/export feature.
Allows exporting student data for sharing or backup.
Allows importing student data from external sources.

CSV Files (data/students.csv)
Used as an import/export feature.
Allows exporting student data in a format compatible
with Excel and Google Sheets for easy viewing.

## Architectural Choices

Object-Oriented Design:
All core entities are modeled as Python classes with
attributes and methods. This ensures encapsulation and
reusability throughout the application.

Modular Architecture:
Each module has a single responsibility:
- Data classes handle entity structure and validation
- StudentManager handles in-memory collection management
- Database module handles all permanent storage
- CLI handles all user interaction
- Logger handles all event tracking
- ConfigManager handles all settings

Singleton Pattern:
ConfigManager uses the Singleton pattern to ensure
only one configuration object exists at any time.

Separation of Concerns:
User interaction (CLI) is completely separated from
business logic (StudentManager, Database) which is
completely separated from data structure (Student, Activity).

Safe SQL:
All database queries use parameterized statements with ?
placeholders to prevent SQL injection.

## Installation

1. Clone the repository:
git clone https://github.com/Melika-Keshavarzi/internship-manager.git

2. Navigate to the project folder:
cd internship-manager

3. Install dependencies:
pip3 install -r requirements.txt

## How to Run the Application

Start the interactive CLI:
python3 main.py

## How to Run Demonstration Scripts

Note: The following are demonstration scripts, not automated
unit tests. They show how each module works independently.

python3 -m src.test_student
python3 -m src.test_relationships
python3 -m src.test_manager
python3 -m src.test_json
python3 -m src.test_csv
python3 -m src.test_validation
python3 -m src.test_database
python3 -m src.test_logger
python3 -m src.test_config
python3 -m src.test_notes_links
python3 -m src.test_reports

## Implemented Functionalities

- Management of student personal information
- Supervisor information management
- Internship and thesis activity registration and tracking
- Management of thesis and internship titles and topics
- Supervision information and activity status tracking
- Management of internship periods and deadlines
- Notes and comments associated with each student
- Storage and organization of useful links
- Management of shared OneDrive folder links
- Management of GitHub repository links
- Registration of related documents
- Filtering and search functionalities
- Activity logging and progress tracking
- Object relationships between students, supervisors, activities
- Data validation: empty fields, email format, enrollment year
- SQLite database with full CRUD operations
- JSON file export and import
- CSV file export and import
- pandas-based data summary
- Centralized logging system
- Configuration management with Singleton pattern
- Interactive command-line interface
- Progress report generation

## Testing Approach

The current scripts in the src/ folder are demonstration
scripts that manually verify each module works correctly.
They are NOT formal automated unit tests.
Formal automated testing using pytest or unittest
is planned as a future development step.

## Problems Encountered and Solutions

ModuleNotFoundError when running scripts:
Solution: Run all scripts from the root directory using
the module flag: python3 -m src.module_name

Empty folders not showing on GitHub:
Solution: Added .gitkeep placeholder files to empty folders

ConfigManager circular import with logger:
Solution: Used try/except fallback in logger.py to handle
cases where ConfigManager is not yet initialized

Database duplicate entries across test runs:
Solution: Used IF NOT EXISTS in CREATE TABLE and
try/except with IntegrityError for INSERT operations

## Weekly Progress Summary

Week 1 (Days 1-5): Setup, Student class, relationships,
manager, JSON storage.

Week 2 (Days 6-10): CSV/pandas, validation, SQLite database,
logging system, configuration management.

Week 3 (Days 11-17): CLI interface, notes/links/documents,
activity tracking, reports, final refinements.

## Developer

Melika Keshavarzi
Data Analysis Student
University of Messina
Supervisor: Professor Francesco La Rosa

Repository: https://github.com/Melika-Keshavarzi/internship-manager