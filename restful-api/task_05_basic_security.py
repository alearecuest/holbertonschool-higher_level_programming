#!/usr/bin/python3
"""
This module implements API security and authentication techniques using Flask.
This module provides routes protected by Basic Authentication
and JWT Authentication, including role-based access control
and consistent error handling.
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

# Configuración JWT
app.config['JWT_SECRET_KEY'] = 'super-strong-secret-key'
jwt = JWTManager(app)

# Base de datos de usuarios (simulada)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the provided username and password for Basic Authentication.
    Returns the username if authentication is successful.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Basic authentication protected route.
    Returns a success message if credentials are valid.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates a user and returns a JWT token.
    Expects JSON payload with username and password.
    Includes the user's role in the JWT claims.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Incluir el rol directamente en la identidad
    token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    JWT protected route.
    Returns a success message if a valid JWT token is provided.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Admin-only protected route.
    Returns a success message if the JWT token is
    valid and the user has admin role. Otherwise, returns
    a 403 Forbidden response.
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Manejadores de errores JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handles missing JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Unauthorized"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handles invalid JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Unauthorized"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handles expired JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(debug=True)
