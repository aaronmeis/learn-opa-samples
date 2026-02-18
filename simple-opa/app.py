from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPA_URL = os.environ.get("OPA_URL", "http://opa:8181/v1/data/rbac/allow")

def check_permission(user, role, method, path):
    input_data = {
        "input": {
            "user": user,
            "role": role,
            "method": method,
            "path": path.strip("/").split("/")
        }
    }
    try:
        response = requests.post(OPA_URL, json=input_data)
        response.raise_for_status()
        return response.json().get("result", False)
    except Exception as e:
        print(f"Error connecting to OPA: {e}")
        return False

@app.before_request
def authorize():
    if request.path in ["/health", "/"]:
        return
        
    user = request.headers.get("X-User-Id", "anonymous")
    role = request.headers.get("X-User-Role", "guest")
    
    if not check_permission(user, role, request.method, request.path):
        return jsonify({"error": "Forbidden"}), 403

@app.route("/")
def index():
    return jsonify({"message": "Simple OPA Flask API"})

@app.route("/public")
def public():
    return jsonify({"message": "This is a public endpoint"})

@app.route("/secure")
def secure():
    return jsonify({"message": "This is a secure endpoint, only for users/admins"})

@app.route("/admin")
def admin():
    return jsonify({"message": "Welcome Admin!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
