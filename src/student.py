class Student:

    def __init__(self, student_id, first_name, last_name, email, phone, enrollment_year, degree_program):
        
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.enrollment_year = enrollment_year
        self.degree_program = degree_program

    def __str__(self):
        
        return f"Student [ID: {self.student_id}] - {self.first_name} {self.last_name} ({self.degree_program})"

    def get_full_name(self):
        
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "enrollment_year": self.enrollment_year,
            "degree_program": self.degree_program
        }


if __name__ == "__main__":
    print("\n=== Running Student Class Test ===")

    
    test_student = Student(
        student_id="5777",
        first_name="Melika",
        last_name="Kshzi",
        email="melika.kshzi@unime.studenti.it",
        phone="+39 000000",
        enrollment_year= 2024,
        degree_program="Data analysis"
    )

 
    print(test_student)

    
    print(f"Full Name: {test_student.get_full_name()}")

  
    print(f"Email: {test_student.email}")

    
    print(f"As Dictionary: {test_student.to_dict()}")

    print("===================================\n")
