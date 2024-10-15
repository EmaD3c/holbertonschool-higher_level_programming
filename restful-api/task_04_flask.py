#!/usr/bin/python3
'''
Flask REST API for handling user data
'''
from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users in a dictionary (in memory)
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# List all usernames in the dictionary
@app.route("/data")
def list_user():
    return jsonify(list(users.keys()))


# Simple status endpoint
@app.route("/status")
def status():
    return "OK"


# Get user data by username
@app.route("/users/<username>")
def get_username(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Add a new user (POST request)
@app.route("/add_user", methods=["POST"])
def post_requests():
    data = request.get_json()

    # Check for required fields
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    # Create the user dictionary and add to the users dict
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
