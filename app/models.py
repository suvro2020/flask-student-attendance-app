from app.database import get_db_connection

def add_student(name):
    """Insert a new student and return their ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    student_id = cursor.lastrowid  # Get last inserted student ID
    conn.commit()
    cursor.close()
    conn.close()
    return student_id

def mark_attendance(student_id, date, status="Present"):
    """Mark attendance for a student."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)", 
                   (student_id, date, status))
    conn.commit()
    cursor.close()
    conn.close()

def get_attendance():
    """Fetch attendance records."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id AS student_id, s.name, a.date, a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC
    """)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
