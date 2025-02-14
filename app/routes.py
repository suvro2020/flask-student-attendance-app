from flask import request, jsonify, render_template
from app import app
from app.models import add_student, mark_attendance, get_attendance
from datetime import date

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register_student', methods=['POST'])
def register_student():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    student_id = add_student(name)
    mark_attendance(student_id, str(date.today()), "Present")

    return jsonify({"message": f"Attendance recorded for {name}!"})

@app.route('/mark_absent', methods=['POST'])
def mark_absent():
    data = request.get_json()
    student_id = data.get("student_id")

    if not student_id:
        return jsonify({"error": "Student ID is required"}), 400

    mark_attendance(student_id, str(date.today()), "Absent")

    return jsonify({"message": "Student marked as Absent!"})

@app.route('/get_attendance', methods=['GET'])
def fetch_attendance():
    records = get_attendance()
    return render_template("attendance.html", records=records)
