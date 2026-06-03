import sqlite3
import os
from src.logger import get_logger
from src.config_manager import ConfigManager

logger = get_logger("database")
config = ConfigManager()
DATABASE_PATH = config.get_database_path()

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Core student data table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            enrollment_year INTEGER,
            degree_program TEXT
        )
    """)

    # Supervisor tracking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS supervisors (
            supervisor_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            department TEXT
        )
    """)

    # Activity/Internship timeline tracking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            activity_id TEXT PRIMARY KEY,
            activity_type TEXT NOT NULL,
            title TEXT NOT NULL,
            topic TEXT,
            start_date TEXT,
            end_date TEXT,
            status TEXT,
            student_id TEXT,
            supervisor_id TEXT,
            FOREIGN KEY (student_id) REFERENCES students (student_id),
            FOREIGN KEY (supervisor_id) REFERENCES supervisors (supervisor_id)
        )
    """)

    # One-to-Many relational table: Notes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            note_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            date TEXT NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
    """)

    # One-to-Many relational table: Links (GitHub, OneDrive, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS links (
            link_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            link_type TEXT NOT NULL,
            url TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
    """)

    # One-to-Many relational table: Document Metadata
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            file_path TEXT NOT NULL,
            description TEXT,
            upload_date TEXT,
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
    """)

    conn.commit()
    conn.close()
    logger.info("Database initialized with all relational target framework tables")
    print("Database initialized successfully!")

def insert_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students
            (student_id, first_name, last_name, email, phone, enrollment_year, degree_program)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            student.student_id,
            student.first_name,
            student.last_name,
            student.email,
            student.phone,
            student.enrollment_year,
            student.degree_program
        ))
        conn.commit()
        logger.info(f"Student inserted: {student.student_id}")
        print(f"Student {student.get_full_name()} inserted into database!")
        return True
    except sqlite3.IntegrityError:
        logger.warning(f"Duplicate student ID hit on raw insertion: {student.student_id}")
        print(f"Student ID {student.student_id} already exists!")
        return False
    finally:
        conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_student(student_id, first_name, last_name, email, phone, enrollment_year, degree_program):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET first_name = ?, last_name = ?, email = ?,
            phone = ?, enrollment_year = ?, degree_program = ?
        WHERE student_id = ?
    """, (first_name, last_name, email, phone, enrollment_year, degree_program, student_id))
    conn.commit()
    conn.close()
    logger.info(f"Student updated: {student_id}")
    print(f"Student {student_id} updated successfully!")

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    logger.info(f"Student deleted: {student_id}")
    print(f"Student {student_id} deleted from database!")

def search_students(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM students
        WHERE first_name LIKE ?
        OR last_name LIKE ?
        OR degree_program LIKE ?
        OR student_id LIKE ?
        OR email LIKE ?
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))
    rows = cursor.fetchall()
    conn.close()
    logger.debug(f"Search for '{keyword}': {len(rows)} results")
    return rows

# === NOTES OPERATIONS ===
def add_note(student_id, date, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notes (student_id, date, content)
        VALUES (?, ?, ?)
    """, (student_id, date, content))
    conn.commit()
    conn.close()
    logger.info(f"Note added for student: {student_id}")
    print(f"Note added for student {student_id}!")

def get_notes(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM notes WHERE student_id = ?
        ORDER BY date DESC
    """, (student_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE note_id = ?", (note_id,))
    conn.commit()
    conn.close()
    logger.info(f"Note dropped from schema row: {note_id}")
    print(f"Note {note_id} deleted!")

# === LINKS OPERATIONS ===
def add_link(student_id, link_type, url, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO links (student_id, link_type, url, description)
        VALUES (?, ?, ?, ?)
    """, (student_id, link_type, url, description))
    conn.commit()
    conn.close()
    logger.info(f"Link added for student: {student_id}")
    print(f"Link added for student {student_id}!")

def get_links(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM links WHERE student_id = ?
    """, (student_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_link(link_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM links WHERE link_id = ?", (link_id,))
    conn.commit()
    conn.close()
    logger.info(f"Link dropped from schema row: {link_id}")
    print(f"Link {link_id} deleted!")

# === DOCUMENTS OPERATIONS ===
def add_document(student_id, file_path, description, upload_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO documents (student_id, file_path, description, upload_date)
        VALUES (?, ?, ?, ?)
    """, (student_id, file_path, description, upload_date))
    conn.commit()
    conn.close()
    logger.info(f"Document added for student: {student_id}")
    print(f"Document added for student {student_id}!")

def get_documents(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM documents WHERE student_id = ?
        ORDER BY upload_date DESC
    """, (student_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_document(doc_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM documents WHERE doc_id = ?", (doc_id,))
    conn.commit()
    conn.close()
    logger.info(f"Document metadata record dropped: {doc_id}")
    print(f"Document {doc_id} deleted!")


def insert_supervisor(supervisor):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO supervisors
            (supervisor_id, first_name, last_name, email, department)
            VALUES (?, ?, ?, ?, ?)
        """, (
            supervisor.supervisor_id,
            supervisor.first_name,
            supervisor.last_name,
            supervisor.email,
            supervisor.department
        ))
        conn.commit()
        logger.info(f"Supervisor inserted: {supervisor.supervisor_id}")
        print(f"Supervisor {supervisor.first_name} {supervisor.last_name} inserted!")
        return True
    except sqlite3.IntegrityError:
        logger.warning(f"Duplicate supervisor ID: {supervisor.supervisor_id}")
        print(f"Supervisor ID {supervisor.supervisor_id} already exists!")
        return False
    finally:
        conn.close()

def get_all_supervisors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM supervisors")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_activity(activity):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO activities
            (activity_id, activity_type, title, topic,
             start_date, end_date, status,
             student_id, supervisor_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            activity.activity_id,
            activity.activity_type,
            activity.title,
            activity.topic,
            activity.start_date,
            activity.end_date,
            activity.status,
            activity.student.student_id,
            activity.supervisor.supervisor_id
        ))
        conn.commit()
        logger.info(f"Activity inserted: {activity.activity_id}")
        print(f"Activity '{activity.title}' inserted!")
        return True
    except sqlite3.IntegrityError:
        logger.warning(f"Duplicate activity ID: {activity.activity_id}")
        print(f"Activity ID {activity.activity_id} already exists!")
        return False
    finally:
        conn.close()

def get_all_activities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.*, 
               s.first_name || ' ' || s.last_name as student_name,
               sv.first_name || ' ' || sv.last_name as supervisor_name
        FROM activities a
        LEFT JOIN students s ON a.student_id = s.student_id
        LEFT JOIN supervisors sv ON a.supervisor_id = sv.supervisor_id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_activities_by_status(status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.*,
               s.first_name || ' ' || s.last_name as student_name,
               sv.first_name || ' ' || sv.last_name as supervisor_name
        FROM activities a
        LEFT JOIN students s ON a.student_id = s.student_id
        LEFT JOIN supervisors sv ON a.supervisor_id = sv.supervisor_id
        WHERE a.status = ?
    """, (status,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_activities_by_type(activity_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.*,
               s.first_name || ' ' || s.last_name as student_name,
               sv.first_name || ' ' || sv.last_name as supervisor_name
        FROM activities a
        LEFT JOIN students s ON a.student_id = s.student_id
        LEFT JOIN supervisors sv ON a.supervisor_id = sv.supervisor_id
        WHERE a.activity_type = ?
    """, (activity_type,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_activity_status(activity_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE activities SET status = ?
        WHERE activity_id = ?
    """, (new_status, activity_id))
    conn.commit()
    conn.close()
    logger.info(f"Activity {activity_id} status updated to {new_status}")
    print(f"Activity {activity_id} status updated to {new_status}!")

def get_upcoming_deadlines(days=30):
    from datetime import date, timedelta
    conn = get_connection()
    cursor = conn.cursor()
    today = str(date.today())
    future = str(date.today() + timedelta(days=days))
    cursor.execute("""
        SELECT a.*,
               s.first_name || ' ' || s.last_name as student_name,
               sv.first_name || ' ' || sv.last_name as supervisor_name
        FROM activities a
        LEFT JOIN students s ON a.student_id = s.student_id
        LEFT JOIN supervisors sv ON a.supervisor_id = sv.supervisor_id
        WHERE a.end_date BETWEEN ? AND ?
        AND a.status != 'completed'
        ORDER BY a.end_date ASC
    """, (today, future))
    rows = cursor.fetchall()
    conn.close()
    return rows