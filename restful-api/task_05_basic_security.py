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
    jwt_required, get_jwt_identity, get_jwt)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'super-strong-secret-key'

jwt = JWTManager(app)

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
    # Eliminar código duplicado y simplificar
    if not username or not password:
        return None
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """
    Handles unauthorized access attempts for Basic Authentication.
    Returns a 401 Unauthorized response.
    """
    # Usar un formato específico para la respuesta
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Basic authentication protected route.
    Returns a success message if credentials are valid.
    """
    return jsonify(message="Basic Auth: Access Granted")


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates a user and returns a JWT token.
    Expects JSON payload with username and password.
    Includes the user's role in the JWT claims.
    """
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 401
    
    # Usar valores predeterminados vacíos
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    JWT protected route.
    Returns a success message if a valid JWT token is provided.
    """
    return jsonify(message="JWT Auth: Access Granted")


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Admin-only protected route.
    Returns a success message if the JWT token is
    valid and the user has admin role. Otherwise, returns
    a 403 Forbidden response.
    """
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handles missing or invalid JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handles invalid JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handles expired JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handles revoked JWT token errors.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handles errors requiring a fresh JWT token.
    Returns a 401 Unauthorized response.
    """
    return jsonify({"error": "Fresh token required"}), 401


@app.errorhandler(401)
def custom_401(error):
    """
    Custom handler for 401 Unauthorized errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def custom_403(error):
    """
    Custom handler for 403 Forbidden errors.
    """
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run(debug=True)
