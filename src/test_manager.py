from src.student import Student
from src.student_manager import StudentManager

manager = StudentManager()

student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")

student2 = Student("5888", "Erfan", "Ghn",
                   "erfan@unime.it", "+39 111111", 2025, "Data Analysis")

student3 = Student("5999", "Yara", "Frz",
                   "yara@unime.it", "+39 222222", 2023, "Artificial Intelligence")

print("\n--- Adding Students ---")
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("\n--- Adding Duplicate (should fail) ---")
manager.add_student(student1)

print("\n--- List All Students ---")
manager.list_all_students()

print("\n--- Find by ID ---")
found = manager.find_by_id("5888")
if found:
    print(f"Found: {found}")
else:
    print("Student not found!")

print("\n--- Search by Name ---")
results = manager.find_by_name("melika")
for s in results:
    print(f"Found: {s}")

print("\n--- Filter by Program ---")
results = manager.filter_by_program("data analysis")
print(f"Students in Data Analysis: {len(results)}")
for s in results:
    print(s)

print("\n--- Remove a Student ---")
manager.remove_student("5999")

print("\n--- List After Removal ---")
manager.list_all_students()