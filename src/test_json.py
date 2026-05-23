from src.student import Student
from src.student_manager import StudentManager

manager = StudentManager()

student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")

student2 = Student("5888", "Erfan", "Ghn",
                   "erfan@unime.it", "+39 111111", 2025, "Data Analysis")

student3 = Student("5999", "Yara", "Frz",
                   "yara@unime.it", "+39 222222", 2023, "Artificial Intelligence")

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("\n--- Saving to JSON file ---")
manager.save_to_json("data/students.json")

print("\n--- Creating empty manager ---")
manager2 = StudentManager()
print("Manager 2 students before loading:")
manager2.list_all_students()

print("\n--- Loading from JSON file ---")
manager2.load_from_json("data/students.json")

print("\n--- Manager 2 students after loading ---")
manager2.list_all_students()

print("\n--- Verifying data is correct ---")
found = manager2.find_by_id("5777")
if found:
    print(f"Found after reload: {found}")
    print(f"Email still intact: {found.email}")