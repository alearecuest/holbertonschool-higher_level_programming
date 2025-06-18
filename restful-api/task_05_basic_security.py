#!/usr/bin/python3
"""
This module implements API security and authentication techniques using Flask.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key para JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Usuarios en memoria
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
}

# --- Basic Auth ---
@auth.verify_password
def verify_password(username, password):
    """Verify username and password."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected endpoint using basic auth."""
    return "Basic Auth: Access Granted"

# --- JWT Login ---
@app.route("/login", methods=["POST"])
def login():
    """Generate JWT token for valid credentials."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"access_token": token})

# --- JWT Protected ---
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT protected endpoint."""
    return "JWT Auth: Access Granted"

# --- Admin Only Route ---
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Admin-only protected endpoint."""
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- JWT Error Handlers ---
@jwt.unauthorized_loader
def handle_unauthorized(err):
    """Handle missing JWT token."""
    return jsonify({"error": "Unauthorized"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Unauthorized"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    """Handle expired JWT token."""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(401)
def custom_401(error):
    """Custom handler for 401 Unauthorized errors."""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def custom_403(error):
    """Custom handler for 403 Forbidden errors."""
    return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run(debug=True)
