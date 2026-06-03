from datetime import date
from src.database import (
    get_all_students,
    get_all_activities,
    get_activities_by_status,
    get_activities_by_type,
    get_upcoming_deadlines
)
from src.logger import get_logger

logger = get_logger("report_generator")

class ReportGenerator:

    def generate_full_report(self):
        print("\n" + "=" * 50)
        print("         INTERNSHIP MANAGER REPORT")
        print(f"         Generated: {date.today()}")
        print("=" * 50)

        self._student_summary()
        self._activity_summary()
        self._upcoming_deadlines()
        self._activity_by_type()

        print("=" * 50)
        print("           END OF REPORT")
        print("=" * 50 + "\n")
        logger.info("Full report generated")

    def _student_summary(self):
        students = get_all_students()
        print(f"\n📋 STUDENT SUMMARY")
        print(f"─" * 40)
        print(f"Total students registered: {len(students)}")
        if students:
            print("\nRegistered students:")
            for s in students:
                print(f"  • {s['first_name']} {s['last_name']} "
                      f"(ID: {s['student_id']}) - {s['degree_program']}")

    def _activity_summary(self):
        all_activities = get_all_activities()
        active = get_activities_by_status("active")
        pending = get_activities_by_status("pending")
        completed = get_activities_by_status("completed")

        print(f"\n📊 ACTIVITY SUMMARY")
        print(f"─" * 40)
        print(f"Total activities:    {len(all_activities)}")
        print(f"Active:              {len(active)}")
        print(f"Pending:             {len(pending)}")
        print(f"Completed:           {len(completed)}")

    def _upcoming_deadlines(self):
        deadlines = get_upcoming_deadlines(30)
        print(f"\n⏰ UPCOMING DEADLINES (next 30 days)")
        print(f"─" * 40)
        if not deadlines:
            print("No upcoming deadlines in the next 30 days.")
        else:
            for d in deadlines:
                print(f"  • [{d['end_date']}] {d['title']}")
                print(f"    Student: {d['student_name']}")
                print(f"    Status: {d['status'].upper()}")

    def _activity_by_type(self):
        internships = get_activities_by_type("internship")
        thesis = get_activities_by_type("thesis")

        print(f"\n📁 ACTIVITIES BY TYPE")
        print(f"─" * 40)
        print(f"Internships: {len(internships)}")
        for a in internships:
            print(f"  • {a['title']} → {a['student_name']}")

        print(f"Thesis:      {len(thesis)}")
        for a in thesis:
            print(f"  • {a['title']} → {a['student_name']}")

    def generate_student_report(self, student_id):
        from src.database import (
            get_student_by_id,
            get_notes,
            get_links,
            get_documents
        )

        student = get_student_by_id(student_id)
        if not student:
            print(f"Student {student_id} not found!")
            return

        print("\n" + "=" * 50)
        print(f"    STUDENT REPORT: {student['first_name']} {student['last_name']}")
        print(f"    Generated: {date.today()}")
        print("=" * 50)

        print(f"\n👤 PERSONAL INFORMATION")
        print(f"─" * 40)
        print(f"ID:              {student['student_id']}")
        print(f"Name:            {student['first_name']} {student['last_name']}")
        print(f"Email:           {student['email']}")
        print(f"Phone:           {student['phone']}")
        print(f"Program:         {student['degree_program']}")
        print(f"Enrollment Year: {student['enrollment_year']}")

        notes = get_notes(student_id)
        print(f"\n📝 NOTES ({len(notes)} total)")
        print(f"─" * 40)
        if not notes:
            print("No notes recorded.")
        else:
            for note in notes:
                print(f"  [{note['date']}] {note['content']}")

        links = get_links(student_id)
        print(f"\n🔗 LINKS ({len(links)} total)")
        print(f"─" * 40)
        if not links:
            print("No links recorded.")
        else:
            for link in links:
                print(f"  [{link['link_type'].upper()}] {link['url']}")
                print(f"    {link['description']}")

        docs = get_documents(student_id)
        print(f"\n📄 DOCUMENTS ({len(docs)} total)")
        print(f"─" * 40)
        if not docs:
            print("No documents recorded.")
        else:
            for doc in docs:
                print(f"  [{doc['upload_date']}] {doc['file_path']}")
                print(f"    {doc['description']}")

        print("=" * 50 + "\n")
        logger.info(f"Student report generated for: {student_id}")