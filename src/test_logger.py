from src.student import Student
from src.student_manager import StudentManager
from src.logger import get_logger

logger = get_logger("test_logger")

print("=== Testing Logging System ===\n")
logger.info("Starting logging scenario script execution pipeline")

manager = StudentManager()

print("\n--- Adding valid student ---")
student1 = Student("5777", "Melika", "Kshzi",
                   "melika@unime.it", "+39 000000", 2024, "Data Analysis")
manager.add_student(student1)

print("\n--- Adding invalid student (bad email syntax) ---")
bad_student = Student("5778", "Test", "User",
                      "notanemail", "+39 000000", 2024, "Data Analysis")
manager.add_student(bad_student)

print("\n--- Adding duplicate student entry ---")
manager.add_student(student1)

print("\n--- Searching for student row target ---")
result = manager.find_by_id("5777")
if result:
    logger.info(f"Search successfully evaluated: {result.get_full_name()}")

print("\n--- Triggering error handler (Load missing file) ---")
manager.load_from_json("data/nonexistent.json")

logger.info("Logging scenario test completed successfully")
print("\n=== Pipeline Check complete: Look at logs/app.log ===")