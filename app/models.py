from app.database import get_db_connection

def add_student(name):
    """Insert a new student into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

def mark_attendance(student_id, date):
    """Mark a student's attendance."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id, date) VALUES (%s, %s)", (student_id, date))
    conn.commit()
    cursor.close()
    conn.close()

def get_attendance():
    """Retrieve attendance records."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT a.id, s.name, a.date 
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC
    """)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
