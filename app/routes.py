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

    add_student(name)
    return jsonify({"message": "Student registered successfully"}), 201

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance_route():
    data = request.get_json()
    student_id = data.get("student_id")

    if not student_id:
        return jsonify({"error": "Student ID is required"}), 400

    mark_attendance(student_id, str(date.today()))
    return jsonify({"message": "Attendance marked successfully"}), 201

@app.route('/get_attendance', methods=['GET'])
def fetch_attendance():
    records = get_attendance()
    return jsonify(records)
