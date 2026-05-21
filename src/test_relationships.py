from src.student import Student
from src.supervisor import Supervisor
from src.activity import Activity

student = Student(
    student_id="5777",
    first_name="Melika",
    last_name="Kshzi",
    email="melika.kshzi@unime.studenti.it",
    phone="+39 000000",
    enrollment_year=2024,
    degree_program="Data analysis"
)

supervisor = Supervisor(
    supervisor_id="9001",
    first_name="Francesco",
    last_name="La Rosa",
    email="francesco.larosa@unime.it",
    department="MIFT"
)

activity = Activity(
    activity_id="A101",
    activity_type="internship",
    title="Data Analysis Automation System",
    topic="Python & Object-Oriented Software Design",
    start_date="2026-05-01",
    end_date="2026-11-01",
    status="active",
    student=student,
    supervisor=supervisor
)

print("=== Running Object Relationship Test ===")
print(student)
print(supervisor)
print("----------------------------------------")
print(activity)
print("========================================")