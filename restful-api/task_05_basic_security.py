#!/usr/bin/python3
'''
Flask REST API for handling user data with JWT and BasicAuth
'''

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity


# Initialize HTTP Basic Auth and Flask app
auth = HTTPBasicAuth()
app = Flask(__name__)

# Configure JWT secret key
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"

# Configure secret key
app.config["SECRET_KEY"] = "your_secret_key"

# Initialize JWT Manager
jwt = JWTManager(app)

# Example users with hashed passwords
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

# JWT error handlers


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    unauthorized error of JWT
    """

    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    invalid token error of JWT
    """

    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    expired token error of JWT
    """

    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    revoked token error of JWT
    """

    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    needs fresh token error of JWT
    """

    return jsonify({"error": "Fresh token required"}), 401


# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    """Check if username and password are valid"""
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
    return None


# Route to get JWT token after login
@app.route("/login", methods=["POST"])
def user_login():
    """
    new user and return jwt access token
    """

    username = request.json["username"]
    password = request.json["password"]

    user = users.get(username)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify(access_token=access_token), 200


# JWT-protected route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Access route protected by JWT"""
    return "JWT Auth: Access Granted", 200


# Basic Auth-protected route
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Access route protected by Basic Auth"""
    return "Basic Auth: Access Granted", 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Access to admin only."""
    if get_jwt_identity()["role"] != "admin":
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
