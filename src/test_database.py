from src.student import Student
from src.supervisor import Supervisor
from src.database import (
    initialize_database,
    insert_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
    search_students
)

print("=== Testing SQLite Database ===\n")

print("--- Step 1: Initialize Database ---")
initialize_database()

print("\n--- Step 2: Insert Students ---")
student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")

student2 = Student("5888", "Erfan", "Ghn",
                   "erfan@unime.it", "+39 111111", 2025, "Data Analysis")

student3 = Student("5999", "Yara", "Frz",
                   "yara@unime.it", "+39 222222", 2023, "Artificial Intelligence")

insert_student(student1)
insert_student(student2)
insert_student(student3)

print("\n--- Step 3: Get All Students ---")
rows = get_all_students()
for row in rows:
    print(f"ID: {row['student_id']} | Name: {row['first_name']} {row['last_name']} | Program: {row['degree_program']}")

print("\n--- Step 4: Find Student by ID ---")
row = get_student_by_id("5888")
if row:
    print(f"Found: {row['first_name']} {row['last_name']}")
else:
    print("Student not found!")

print("\n--- Step 5: Update a Student ---")
update_student("5888", "Erfan", "Ghn",
               "erfan.new@unime.it", "+39 111111", 2025, "Computer Science")

row = get_student_by_id("5888")
print(f"After update: {row['first_name']} | Email: {row['email']} | Program: {row['degree_program']}")

print("\n--- Step 6: Search Students ---")
results = search_students("data")
print(f"Search results for 'data': {len(results)} found")
for row in results:
    print(f"  {row['first_name']} {row['last_name']} - {row['degree_program']}")

print("\n--- Step 7: Delete a Student ---")
delete_student("5999")

print("\n--- Step 8: Final List ---")
rows = get_all_students()
print(f"Total students remaining: {len(rows)}")
for row in rows:
    print(f"  {row['first_name']} {row['last_name']}")

print("\n=== Database Test Complete ===")