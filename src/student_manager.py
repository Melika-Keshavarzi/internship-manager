import json
import os
import csv
import pandas as pd
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
        print(f"Saved {len(self.students)} students to {filepath}")

    def load_from_json(self, filepath):
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return False
        with open(filepath, "r") as file:
            data = json.load(file)
        self.students = [Student.from_dict(s) for s in data]
        print(f"Loaded {len(self.students)} students from {filepath}")
        return True

    def export_to_csv(self, filepath):
        if len(self.students) == 0:
            print("No students to export!")
            return False
        with open(filepath, "w", newline="") as file:
            fieldnames = ["student_id", "first_name", "last_name",
                         "email", "phone", "enrollment_year", "degree_program"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow(student.to_dict())
        print(f"Exported {len(self.students)} students to {filepath}")
        return True

    def import_from_csv(self, filepath):
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return False
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                row["enrollment_year"] = int(row["enrollment_year"])
                student = Student.from_dict(row)
                if self.add_student(student):
                    count += 1
        print(f"Imported {count} students from {filepath}")
        return True

    def show_summary_with_pandas(self, filepath):
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return
        df = pd.read_csv(filepath)
        print("\n=== Student Summary (pandas) ===")
        print(f"Total students: {len(df)}")
        print(f"\nStudents per program:")
        print(df["degree_program"].value_counts().to_string())
        print(f"\nEnrollment years:")
        print(df["enrollment_year"].value_counts().sort_index().to_string())
        print("=" * 40)