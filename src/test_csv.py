from src.student import Student
from src.student_manager import StudentManager

manager = StudentManager()

student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")

student2 = Student("5888", "Erfan", "Ghn",
                   "erfan@unime.it", "+39 111111", 2025, "Data Analysis")

student3 = Student("5999", "Yara", "Frz",
                   "yara@unime.it", "+39 222222", 2023, "Artificial Intelligence")

student4 = Student("6000", "Marco", "Rossi",
                   "marco@unime.it", "+39 333333", 2023, "Computer Science")

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)
manager.add_student(student4)

print("\n--- Exporting to CSV ---")
manager.export_to_csv("data/students.csv")

print("\n--- Creating new empty manager ---")
manager2 = StudentManager()

print("\n--- Importing from CSV ---")
manager2.import_from_csv("data/students.csv")

print("\n--- Verifying imported students ---")
manager2.list_all_students()

print("\n--- Pandas Summary ---")
manager2.show_summary_with_pandas("data/students.csv")