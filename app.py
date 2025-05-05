# CORAAL SaaS Platform - Starter Code (Python Flask Backend + Placeholder Logic)

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ---------------------------
# Mock Database (In-Memory)
# ---------------------------
users = []
automations = []
reports = []

# ---------------------------
# Utility Functions
# ---------------------------
def generate_id(prefix):
    return f"{prefix}_{datetime.utcnow().timestamp()}"

# ---------------------------
# Routes
# ---------------------------

@app.route("/api/register", methods=["POST"])
def register_user():
    data = request.json
    user = {
        "id": generate_id("user"),
        "name": data.get("name"),
        "email": data.get("email"),
        "joined_at": datetime.utcnow().isoformat()
    }
    users.append(user)
    return jsonify({"message": "User registered", "user": user}), 201

@app.route("/api/create-automation", methods=["POST"])
def create_automation():
    data = request.json
    automation = {
        "id": generate_id("auto"),
        "name": data.get("name"),
        "trigger": data.get("trigger"),
        "action": data.get("action"),
        "created_at": datetime.utcnow().isoformat()
    }
    automations.append(automation)
    return jsonify({"message": "Automation created", "automation": automation}), 201

@app.route("/api/generate-report", methods=["POST"])
def generate_report():
    data = request.json
    report = {
        "id": generate_id("report"),
        "title": data.get("title"),
        "filters": data.get("filters"),
        "generated_at": datetime.utcnow().isoformat(),
        "summary": "This is a mock summary of your report."
    }
    reports.append(report)
    return jsonify({"message": "Report generated", "report": report}), 201

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": users})

@app.route("/api/automations", methods=["GET"])
def get_automations():
    return jsonify({"automations": automations})

@app.route("/api/reports", methods=["GET"])
def get_reports():
    return jsonify({"reports": reports})

# ---------------------------
# Run Server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
