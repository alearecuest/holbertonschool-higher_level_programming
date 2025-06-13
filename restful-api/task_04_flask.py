#!/usr/bin/python3
"""
Simple Flask API Demo

Description:
    This script implements a simple RESTful API using Flask framework.
    It provides endpoints for user management with basic CRUD operations.
    The data is stored in memory (dictionary) for demonstration purposes.

Available Endpoints:
    - GET /: Welcome message
    - GET /data: List all registered usernames
    - GET /status: Server status check
    - GET /users/<username>: Get specific user details
    - POST /add_user: Create a new user
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    """Root endpoint that welcomes to the API"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the server status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """
    Dynamic endpoint that returns information for a specific user
    based on the username provided in the URL
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user
    Accepts JSON data in a POST request
    """
    user_data = request.json

    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data['username']
    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
