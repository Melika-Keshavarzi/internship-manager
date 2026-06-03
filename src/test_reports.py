from src.student import Student
from src.supervisor import Supervisor
from src.activity import Activity
from src.database import (
    initialize_database,
    insert_student,
    insert_supervisor,
    insert_activity,
    update_activity_status,
    get_upcoming_deadlines,
    add_note,
    add_link,
    add_document
)
from src.report_generator import ReportGenerator
from datetime import date, timedelta
import os

print("=== Testing Activity Tracking and Reports ===\n")

if os.path.exists("data/internship_manager.db"):
    os.remove("data/internship_manager.db")
    print("Old database removed!")

initialize_database()

student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")
student2 = Student("5888", "Erfan", "Ghn",
                   "erfan@unime.it", "+39 111111", 2025, "Data Analysis")
student3 = Student("5999", "Yara", "Frz",
                   "yara@unime.it", "+39 222222", 2023, "Artificial Intelligence")

insert_student(student1)
insert_student(student2)
insert_student(student3)

supervisor1 = Supervisor("9001", "Francesco", "La Rosa",
                         "francesco.larosa@unime.it", "MIFT")
insert_supervisor(supervisor1)

today = date.today()
soon = str(today + timedelta(days=15))
later = str(today + timedelta(days=90))
past = str(today - timedelta(days=30))

activity1 = Activity("A001", "internship",
                     "Data Analysis Automation System",
                     "Python and OOP",
                     str(today), soon,
                     "active", student1, supervisor1)

activity2 = Activity("A002", "thesis",
                     "Machine Learning in Healthcare",
                     "AI Applications",
                     str(today), later,
                     "active", student2, supervisor1)

activity3 = Activity("A003", "internship",
                     "Database Management System",
                     "SQLite and Python",
                     past, str(today),
                     "completed", student3, supervisor1)

insert_activity(activity1)
insert_activity(activity2)
insert_activity(activity3)

add_note("5777", str(today), "Started internship orientation successfully.")
add_note("5777", str(today), "First meeting with supervisor completed.")
add_link("5777", "github", "https://github.com/Melika-Keshavarzi", "Student GitHub")
add_link("5777", "onedrive", "https://onedrive.live.com/folder", "Shared folder")
add_document("5777", "data/docs/contract.pdf", "Signed contract", str(today))

print("\n--- Updating activity status ---")
update_activity_status("A003", "completed")

print("\n--- Checking upcoming deadlines ---")
deadlines = get_upcoming_deadlines(30)
print(f"Upcoming deadlines in next 30 days: {len(deadlines)}")

reporter = ReportGenerator()

print("\n--- Generating Full Report ---")
reporter.generate_full_report()

print("\n--- Generating Student Report ---")
reporter.generate_student_report("5777")

print("=== Activity Tracking Test Complete ===")