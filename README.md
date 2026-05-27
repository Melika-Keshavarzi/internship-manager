# Internship Manager

A Python-based management system for organizing and monitoring
internships and thesis activities in an academic environment.

## Project Description

This application supports the organization and monitoring of
interns and thesis students involved in academic and research
activities. It is built using object-oriented Python and follows
a modular architecture with clear separation between data classes
and management logic.

## Project Structure

internship-manager/
├── src/                        Source code modules
│   ├── student.py              Student data class
│   ├── supervisor.py           Supervisor data class
│   ├── activity.py             Activity data class
│   ├── student_manager.py      Collection management and file I/O
│   ├── test_student.py         Demonstration script for Student class
│   ├── test_relationships.py   Demonstration script for class relationships
│   ├── test_manager.py         Demonstration script for StudentManager
│   ├── test_json.py            Demonstration script for JSON persistence
│   └── test_csv.py             Demonstration script for CSV import/export
├── data/                       Exported and sample data files
├── config/                     Configuration files
├── logs/                       Application log files
├── docs/                       Documentation and development log
├── requirements.txt            Project dependencies
├── README.md                   Project documentation
└── .gitignore                  Git ignore rules

## Main Classes

### Student
Represents a student with personal and academic information.
Attributes: student_id, first_name, last_name, email, phone,
enrollment_year, degree_program.
Methods: get_full_name(), to_dict(), from_dict(), validate()

### Supervisor
Represents an academic supervisor.
Attributes: supervisor_id, first_name, last_name, email, department.

### Activity
Represents an internship or thesis activity.
Links a Student object and a Supervisor object together.
Attributes: activity_id, activity_type, title, topic,
start_date, end_date, status, student, supervisor.

### StudentManager
Handles collections of Student objects.
Provides methods for adding, removing, searching, filtering,
and persisting student data to JSON and CSV files.

## Installation

1. Clone the repository:
git clone https://github.com/Melika-Keshavarzi/internship-manager.git

2. Navigate to the project folder:
cd internship-manager

3. Install dependencies:
pip3 install -r requirements.txt

## How to Run Demonstration Scripts

Run these commands from the root project folder:

python3 -m src.test_student
python3 -m src.test_relationships
python3 -m src.test_manager
python3 -m src.test_json
python3 -m src.test_csv
python3 -m src.test_validation

## Implemented Functionalities

- Management of student personal information
- Supervisor information management
- Internship and thesis activity registration
- Object relationships between students, supervisors and activities
- Collection management with search and filter operations
- Data validation including duplicate ID and field checking
- JSON file storage and retrieval
- CSV import and export
- pandas-based data summary

## Developer

Melika Keshavarzi
Data Analysis Student
University of Messina
Supervisor: Professor Francesco La Rosa