#!/usr/bin/python3
'''
Flask REST API for handling user data with JWT and BasicAuth
'''

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity


# Initialize HTTP Basic Auth and Flask app
auth = HTTPBasicAuth()
app = Flask(__name__)

# Configure JWT secret key
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize JWT Manager
jwt = JWTManager(app)

# Example users with hashed passwords
users = {
    "user1": generate_password_hash("password1"),
    "admin": generate_password_hash("adminpassword")
}


# JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing or invalid JWT"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid JWT"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles expired JWT"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles revoked JWT"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles requests that need a fresh JWT"""
    return jsonify({"error": "Fresh token required"}), 401


# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    """Verifies username and password with Basic Auth"""
    if username in users:
        return check_password_hash(users[username], password)
    return False


# Route to get JWT token after login
@app.route("/login", methods=["POST"])
def user_login():
    """Authenticates user and returns JWT token"""
    username = request.json["username"]
    password = request.json["password"]

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username})
    return jsonify(access_token=access_token), 200


# JWT-protected route
@app.route('/jwt_protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route requiring a valid JWT"""
    current_user = get_jwt_identity()
    return jsonify({"message": f"Welcome, {current_user['username']}!"}), 200


# Basic Auth-protected route
@app.route('/hash_protected')
@auth.login_required
def hash_protected():
    """Protected route requiring Basic Auth"""
    return jsonify({"message": "Password hash and check succeeded!"})


# Route to hash and verify password
@app.route('/hash', methods=['POST'])
def hash_password():
    """Hashes a given password and verifies it"""
    data = request.get_json()
    if 'password' not in data:
        return jsonify({"error": "Password is required"}), 400

    hashed_password = generate_password_hash(data['password'])

    if not check_password_hash(hashed_password, data['password']):
        return jsonify({"error": "Password did not correspond"}), 400

    return jsonify({"hashed_password": hashed_password})


if __name__ == '__main__':
    app.run(debug=True)
