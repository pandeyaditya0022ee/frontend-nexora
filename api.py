from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

# Mock Data (Replace with database queries)
student_profile = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "course": "Computer Science",
    "year": "3rd Year"
}

academic_records = [
    {"semester": 1, "gpa": 3.8, "courses": ["Math", "Physics", "CS101"]},
    {"semester": 2, "gpa": 3.9, "courses": ["Calculus", "Electronics", "CS102"]}
]

financial_records = {
    "total_fees": 5000,
    "paid": 3000,
    
    "pending": 2000,
    "transactions": [
        {"id": 101, "amount": 1500, "date": "2023-01-15", "status": "Paid"},
        {"id": 102, "amount": 1500, "date": "2023-06-15", "status": "Paid"}
    ]
}

tasks = [
    {"id": 1, "title": "Submit Assignment", "due_date": "2023-11-30", "completed": False},
    {"id": 2, "title": "Register for Exams", "due_date": "2023-12-05", "completed": False}
]

skills = ["Python", "JavaScript", "Data Analysis", "Machine Learning"]

@api.route('/profile', methods=['GET'])
def get_profile():
    """Get student profile information"""
    return jsonify(student_profile)

@api.route('/academic', methods=['GET'])
def get_academic():
    """Get academic records"""
    return jsonify(academic_records)

@api.route('/financial', methods=['GET'])
def get_financial():
    """Get financial status and history"""
    return jsonify(financial_records)

@api.route('/tasks', methods=['GET'])
def get_tasks():
    """Get list of tasks"""
    return jsonify(tasks)

@api.route('/tasks', methods=['POST'])
def add_task():
    """Add a new task"""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "due_date": data.get('due_date', ''),
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@api.route('/skills', methods=['GET'])
def get_skills():
    """Get list of skills"""
    return jsonify(skills)

@api.route('/skills', methods=['POST'])
def add_skill():
    """Add a new skill"""
    data = request.get_json()
    if not data or 'skill' not in data:
        return jsonify({"error": "Skill is required"}), 400
    
    skills.append(data['skill'])
    return jsonify({"message": "Skill added", "skills": skills}), 201
