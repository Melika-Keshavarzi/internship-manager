from src.student import Student
from src.database import (
    initialize_database,
    insert_student,
    add_note,
    get_notes,
    delete_note,
    add_link,
    get_links,
    delete_link,
    add_document,
    get_documents,
    delete_document
)
from datetime import date

print("=== Testing Notes, Links and Documents System ===\n")

# Re-run initialization to verify safety parameters and build new tables
initialize_database()

# Create a sample student target record
student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")
insert_student(student1)

print("\n--- Adding Relational Notes ---")
add_note("5777", str(date.today()), "Student started internship orientation.")
add_note("5777", str(date.today()), "First meeting with supervisor completed.")
add_note("5777", str(date.today()), "Research topic confirmed: Data Analysis Automation.")

print("\n--- Reading Committed Notes ---")
notes = get_notes("5777")
print(f"Total notes found for student 5777: {len(notes)}")
for note in notes:
    print(f"  [{note['date']}] {note['content']}")

print("\n--- Adding Hyperlink References ---")
add_link("5777", "github", "https://github.com/Melika-Keshavarzi", "Student GitHub profile")
add_link("5777", "onedrive", "https://onedrive.live.com/student-folder", "Shared OneDrive folder")
add_link("5777", "other", "https://unime.it/thesis-guidelines", "Thesis guidelines")

print("\n--- Reading Committed Links ---")
links = get_links("5777")
print(f"Total links found for student 5777: {len(links)}")
for link in links:
    print(f"  [{link['link_type'].upper()}] {link['url']}")
    print(f"    Description: {link['description']}")

print("\n--- Registering Document Paths ---")
add_document("5777", "data/docs/internship_contract.pdf",
             "Signed internship contract", str(date.today()))
add_document("5777", "data/docs/thesis_proposal.pdf",
             "Initial thesis proposal", str(date.today()))

print("\n--- Reading Registered Documents ---")
docs = get_documents("5777")
print(f"Total documents registered for student 5777: {len(docs)}")
for doc in docs:
    print(f"  [{doc['upload_date']}] {doc['file_path']}")
    print(f"    Description: {doc['description']}")

print("\n--- Testing Single Row Record Deletion ---")
# Extract the ID of the first retrieved note to test isolation removal
first_note_id = notes[0]['note_id']
delete_note(first_note_id)

notes_after = get_notes("5777")
print(f"Notes remaining after isolation wipe: {len(notes_after)}")

print("\n=== Notes, Links and Documents Test Complete ===")