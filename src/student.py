class Student:

    VALID_PROGRAMS = [
        "data analysis",
        "computer science",
        "engineering",
        "artificial intelligence",
        "mathematics",
        "physics"
    ]

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

    def validate(self):
        errors = []

        if not self.student_id or self.student_id.strip() == "":
            errors.append("Student ID cannot be empty")

        if not self.first_name or self.first_name.strip() == "":
            errors.append("First name cannot be empty")

        if not self.last_name or self.last_name.strip() == "":
            errors.append("Last name cannot be empty")

        if not self.email or "@" not in self.email:
            errors.append("Email is not valid")

        if not self.phone or self.phone.strip() == "":
            errors.append("Phone cannot be empty")

        if not isinstance(self.enrollment_year, int):
            errors.append("Enrollment year must be a number")
        elif self.enrollment_year < 2000 or self.enrollment_year > 2030:
            errors.append("Enrollment year must be between 2000 and 2030")

        if not self.degree_program or self.degree_program.strip() == "":
            errors.append("Degree program cannot be empty")

        return errors