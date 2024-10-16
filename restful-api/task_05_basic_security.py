from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialisation de l'authentification HTTP basique
auth = HTTPBasicAuth()

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la clé secrète nécessaire pour JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialisation du gestionnaire JWT
jwt = JWTManager(app)

# Liste d'utilisateurs avec mots de passe hachés (exemple)
users = {
    "user1": generate_password_hash("password1"),
    "admin": generate_password_hash("adminpassword")
}


# Gestion des erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Fonction pour vérifier les identifiants fournis par l'utilisateur
@auth.verify_password
def verify_password(username, password):
    if username in users:
        # Vérification du mot de passe en clair avec le mot de passe haché
        return check_password_hash(users[username], password)
    return False


# Route protégée par JWT
@app.route('/jwt_protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    # Récupère l'identité (nom d'utilisateur) depuis le JWT
    current_user = get_jwt_identity()
    return jsonify({"message": f"Welcome, {current_user}!"}), 200


# Route protégée par authentification basique
@app.route('/hash_protected')
@auth.login_required
def hash_protected():
    # Si l'authentification réussit, retourne un message
    return jsonify({"message": "Password hash and check succeeded!"})


# Route pour tester le hashage et la vérification des mots de passe
@app.route('/hash', methods=['POST'])
def hash_password():
    data = request.get_json()
    if 'password' not in data:
        return jsonify({"error": "Password is required"}), 400

    # Hachage du mot de passe
    hashed_password = generate_password_hash(data['password'])

    # Vérification du mot de passe (hash) si besoin
    if not check_password_hash(hashed_password, data['password']):
        return jsonify({"error": "Password did not correspond"}), 400

    return jsonify({"hashed_password": hashed_password})


if __name__ == '__main__':
    app.run(debug=True)
