import json
import os
from src.student import Student

class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing in self.students:
            if existing.student_id == student.student_id:
                print(f"Student with ID {student.student_id} already exists!")
                return False
        self.students.append(student)
        print(f"Student {student.get_full_name()} added successfully!")
        return True

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.get_full_name()} removed!")
                return True
        print(f"No student found with ID {student_id}")
        return False

    def find_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_by_name(self, name):
        name = name.lower()
        results = [s for s in self.students
                   if name in s.get_full_name().lower()]
        return results

    def list_all_students(self):
        if len(self.students) == 0:
            print("No students in the system!")
            return
        print(f"\n=== All Students ({len(self.students)} total) ===")
        for student in self.students:
            print(student)
        print("=" * 40)

    def filter_by_program(self, program):
        program = program.lower()
        results = [s for s in self.students
                   if program in s.degree_program.lower()]
        return results

    def save_to_json(self, filepath):
        data = [student.to_dict() for student in self.students]
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Successfully saved {len(self.students)} students to {filepath}")

    def load_from_json(self, filepath):
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return False
        with open(filepath, "r") as file:
            data = json.load(file)
        self.students = [Student.from_dict(s) for s in data]
        print(f"Successfully loaded {len(self.students)} students from {filepath}")
        return True