import mysql.connector
import os
import time

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "rootpassword"),
    "database": os.getenv("DB_NAME", "attendance_db")
}

def get_db_connection(retries=5, delay=5):
    """Try to connect to MySQL with retries."""
    for attempt in range(retries):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            print("Connected to MySQL successfully!")
            return conn
        except mysql.connector.Error as err:
            print(f"Attempt {attempt+1}: MySQL connection failed ({err})")
            time.sleep(delay)
    raise Exception("Failed to connect to MySQL after multiple attempts.")

def init_db():
    """Initialize the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS attendance_db")
    cursor.execute("USE attendance_db")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
