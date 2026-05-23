class Student:

    def __init__(self, student_id, first_name, last_name,
                 email, phone, enrollment_year, degree_program):
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

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data["phone"],
            enrollment_year=data["enrollment_year"],
            degree_program=data["degree_program"]
        )