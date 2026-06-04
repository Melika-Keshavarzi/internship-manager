# Internship Manager

A Python-based management system for organizing and monitoring
internships and thesis activities in an academic environment.

## Project Description

This application supports the organization and monitoring of
interns and thesis students involved in academic and research
activities. It is built using object-oriented Python and follows
a modular architecture with clear separation between data classes,
management logic, persistence, and user interaction.

## Project Structure

internship-manager/
├── src/
│   ├── student.py              Student data class with validation
│   ├── supervisor.py           Supervisor data class
│   ├── activity.py             Activity data class (internship/thesis)
│   ├── student_manager.py      Collection management and file I/O
│   ├── database.py             SQLite database layer (all CRUD operations)
│   ├── logger.py               Centralized logging configuration
│   ├── config_manager.py       Configuration management (Singleton)
│   ├── report_generator.py     Progress and status report generation engine
│   ├── cli.py                  Interactive command-line interface
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
│   └── test_reports.py         Demonstration script for activity tracking and reports
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

### StudentManager (src/student_manager.py)
Handles collections of Student objects in memory.
Provides methods for adding, removing, searching, filtering,
and persisting student data to JSON and CSV files.
Note: This class manages in-memory collections.
For permanent storage, the SQLite database layer is used.

### Database (src/database.py)
SQLite database layer for permanent data storage.
Contains functions for full CRUD operations on students,
supervisors, activities, notes, links, and documents.
This is the main persistence mechanism of the application.
JSON and CSV are used as import/export and demonstration features.

### Logger (src/logger.py)
Centralized logging configuration using Python logging library.
Writes logs to both the terminal and logs/app.log file.
Uses RotatingFileHandler to manage log file size automatically.
Log levels used: DEBUG, INFO, WARNING, ERROR.

### ConfigManager (src/config_manager.py)
Reads and applies settings from config/config.json.
Implements the Singleton design pattern.
Provides fallback default values if config file is missing.
All modules read their paths and settings from this class.

### ReportGenerator (src/report_generator.py)
Compiles complex information across multiple relational tables into clear, actionable summaries. Generates full high-level overviews as well as focused student progress dossiers containing their exact logged history.

### CLI (src/cli.py)
Interactive command-line interface for the application.
Provides a menu-driven system for all student operations.
Completely separated from business logic.

### main.py
Single entry point for the application.
Run this file to start the interactive CLI.

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
- Internship and thesis activity registration
- Object relationships between students, supervisors, activities
- Collection management with search and filter operations
- Data validation: empty fields, email format, enrollment year
- SQLite database with full CRUD operations
- Notes management per student
- Links management per student (GitHub, OneDrive, other)
- Document registration per student
- Activity tracking with status management
- Progress reports with upcoming deadlines
- Student individual reports with full details
- Report generation combining all data sources
- JSON file export and import
- CSV file export and import
- pandas-based data summary
- Centralized logging system
- Configuration management with Singleton pattern
- Interactive command-line interface

## Testing Approach

The current scripts in the src/ folder are demonstration
scripts that manually verify each module works correctly.
They are NOT formal automated unit tests.
Formal automated testing using pytest or unittest
is planned as a future development step.

## Developer

Melika Keshavarzi
Data Analysis Student
University of Messina
Supervisor: Professor Francesco La Rosa