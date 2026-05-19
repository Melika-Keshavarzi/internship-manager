from src.student import Student

student_dict = {
    "student_id": "5777",
    "first_name": "Melika",
    "last_name": "Kshzi",
    "email": "melika.kshzi@unime.studenti.it",
    "phone": "+39 000000",
    "enrollment_year": 2024,
    "degree_program": "Data analysis"
}

students_list = [
    student_dict,
    {
        "student_id": "5888",
        "first_name": "Erfan",
        "last_name": "Ghn",
        "email": "erfan.ghn@unime.studenti.it",
        "phone": "+39 111111",
        "enrollment_year": 2025,
        "degree_program": "Data analysis"
    },
    {
        "student_id": "5999",
        "first_name": "Yara",
        "last_name": "Frz",
        "email": "yara.frz@unime.studenti.it",
        "phone": "+39 222222",
        "enrollment_year": 2023,
        "degree_program": "Artificial Intelligence"
    }
]

print("=== Running Student Class Verification ===")

student1 = Student(
    student_id=student_dict["student_id"],
    first_name=student_dict["first_name"],
    last_name=student_dict["last_name"],
    email=student_dict["email"],
    phone=student_dict["phone"],
    enrollment_year=student_dict["enrollment_year"],
    degree_program=student_dict["degree_program"]
)

print(student1)
print(f"Full Name Method Output: {student1.get_full_name()}")
print(f"Dictionary Method Output: {student1.to_dict()}")

print("\n--- Processing and Printing All Students From the List ---")
for s in students_list:
    student_obj = Student(
        student_id=s["student_id"],
        first_name=s["first_name"],
        last_name=s["last_name"],
        email=s["email"],
        phone=s["phone"],
        enrollment_year=s["enrollment_year"],
        degree_program=s["degree_program"]
    )
    print(student_obj)

print("==========================================")