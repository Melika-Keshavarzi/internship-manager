from src.student import Student
from src.student_manager import StudentManager
from src.config_manager import ConfigManager
from src.logger import get_logger

logger = get_logger("cli")
config = ConfigManager()
config.load()

def print_header():
    print("\n" + "=" * 42)
    print(f"     INTERNSHIP MANAGER v{config.get_app_version()}")
    print("=" * 42)

def print_menu():
    print_header()
    print("1.  Add new student")
    print("2.  View all students")
    print("3.  Search student by ID")
    print("4.  Search student by name")
    print("5.  Filter by degree program")
    print("6.  Remove student")
    print("7.  Save students to JSON")
    print("8.  Load students from JSON")
    print("9.  Export students to CSV")
    print("10. Import students from CSV")
    print("0.  Exit")
    print("=" * 42)

def get_student_input():
    print("\n--- Enter Student Information ---")
    student_id = input("Student ID: ").strip()
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()

    while True:
        try:
            enrollment_year = int(input("Enrollment Year: ").strip())
            break
        except ValueError:
            print("Please enter a valid year (example: 2024)")

    degree_program = input("Degree Program: ").strip()

    return Student(
        student_id,
        first_name,
        last_name,
        email,
        phone,
        enrollment_year,
        degree_program
    )

def handle_add_student(manager):
    try:
        student = get_student_input()
        manager.add_student(student)
    except KeyboardInterrupt:
        print("\nCancelled.")

def handle_search_by_id(manager):
    student_id = input("\nEnter Student ID: ").strip()
    result = manager.find_by_id(student_id)
    if result:
        print(f"\nFound: {result}")
        print(f"Email: {result.email}")
        print(f"Phone: {result.phone}")
        print(f"Program: {result.degree_program}")
        print(f"Year: {result.enrollment_year}")
    else:
        print(f"No student found with ID: {student_id}")

def handle_search_by_name(manager):
    name = input("\nEnter name to search: ").strip()
    results = manager.find_by_name(name)
    if results:
        print(f"\nFound {len(results)} student(s):")
        for student in results:
            print(f"  {student}")
    else:
        print(f"No students found with name: {name}")

def handle_filter_by_program(manager):
    program = input("\nEnter degree program: ").strip()
    results = manager.filter_by_program(program)
    if results:
        print(f"\nFound {len(results)} student(s) in {program}:")
        for student in results:
            print(f"  {student}")
    else:
        print(f"No students found in program: {program}")

def handle_remove_student(manager):
    student_id = input("\nEnter Student ID to remove: ").strip()
    confirm = input(f"Are you sure you want to remove student {student_id}? (yes/no): ").strip().lower()
    if confirm == "yes":
        manager.remove_student(student_id)
    else:
        print("Removal cancelled.")

def handle_save_json(manager):
    filepath = input(f"\nEnter filepath (press Enter for default: data/students.json): ").strip()
    if filepath == "":
        filepath = "data/students.json"
    manager.save_to_json(filepath)

def handle_load_json(manager):
    filepath = input(f"\nEnter filepath (press Enter for default: data/students.json): ").strip()
    if filepath == "":
        filepath = "data/students.json"
    manager.load_from_json(filepath)

def handle_export_csv(manager):
    filepath = input(f"\nEnter filepath (press Enter for default: data/students.csv): ").strip()
    if filepath == "":
        filepath = "data/students.csv"
    manager.export_to_csv(filepath)

def handle_import_csv(manager):
    filepath = input(f"\nEnter filepath (press Enter for default: data/students.csv): ").strip()
    if filepath == "":
        filepath = "data/students.csv"
    manager.import_from_csv(filepath)

def run():
    logger.info("CLI started")
    manager = StudentManager()

    print_header()
    print("Welcome to the Internship Manager!")

    while True:
        print_menu()

        choice = input("Choose an option: ").strip()
        logger.debug(f"User selected option: {choice}")

        if choice == "1":
            handle_add_student(manager)
        elif choice == "2":
            manager.list_all_students()
        elif choice == "3":
            handle_search_by_id(manager)
        elif choice == "4":
            handle_search_by_name(manager)
        elif choice == "5":
            handle_filter_by_program(manager)
        elif choice == "6":
            handle_remove_student(manager)
        elif choice == "7":
            handle_save_json(manager)
        elif choice == "8":
            handle_load_json(manager)
        elif choice == "9":
            handle_export_csv(manager)
        elif choice == "10":
            handle_import_csv(manager)
        elif choice == "0":
            logger.info("CLI exited by user")
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()