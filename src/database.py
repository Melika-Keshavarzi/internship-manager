import sqlite3
import os

DATABASE_PATH = "data/internship_manager.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS supervisors (
            supervisor_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            department TEXT
        )
    """)

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

    conn.commit()
    conn.close()
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
        print(f"Student {student.get_full_name()} inserted into database!")
        return True
    except sqlite3.IntegrityError:
        print(f"Student ID {student.student_id} already exists in database!")
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
    print(f"Student {student_id} updated successfully!")

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"Student {student_id} deleted from database!")

def search_students(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM students
        WHERE first_name LIKE ? OR last_name LIKE ? OR degree_program LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()
    conn.close()
    return rows