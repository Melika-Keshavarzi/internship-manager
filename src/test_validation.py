from src.student import Student
from src.student_manager import StudentManager

manager = StudentManager()

print("=== Testing Data Validation Engine ===\n")

print("--- Case 1: Valid student (Should pass) ---")
valid_student = Student("5777", "Melika", "Kshzi",
                        "melika@unime.it", "+39 000000",
                        2024, "Data Analysis")
manager.add_student(valid_student)

print("\n--- Case 2: Missing first name (Should fail) ---")
no_name = Student("5778", "", "Kshzi",
                  "test@unime.it", "+39 000000",
                  2024, "Data Analysis")
manager.add_student(no_name)

print("\n--- Case 3: Invalid email syntax (Should fail) ---")
bad_email = Student("5779", "Test", "User",
                    "notanemail.com", "+39 000000",
                    2024, "Data Analysis")
manager.add_student(bad_email)

print("\n--- Case 4: Extreme Out-of-bounds Year (Should fail) ---")
bad_year = Student("5780", "Test", "User",
                   "test@unime.it", "+39 000000",
                   1850, "Data Analysis")
manager.add_student(bad_year)

print("\n--- Case 5: Blank Student ID string (Should fail) ---")
no_id = Student("   ", "Test", "User",
                "test@unime.it", "+39 000000",
                2024, "Data Analysis")
manager.add_student(no_id)

print("\n--- Case 6: Duplicate ID insertion (Should fail) ---")
duplicate = Student("5777", "Another", "Person",
                    "another@unime.it", "+39 999999",
                    2023, "Computer Science")
manager.add_student(duplicate)

print("\n--- Current Final Checked List ---")
manager.list_all_students()