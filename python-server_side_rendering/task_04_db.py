import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')


# Route pour la page "About"
@app.route('/about')
def about():
    return render_template('about.html')


# Route pour la page "Contact"
@app.route('/contact')
def contact():
    return render_template('contact.html')


# La route /items lit le fichier JSON des articles
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_data = data.get("items", [])
    except FileNotFoundError:
        item_data = []

    return render_template('items.html', items=item_data)


# Fonction auxiliaire pour lire les données JSON à partir d'un fichier
def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Fonction auxiliaire pour lire les données CSV à partir d'un fichier
def read_csv_file(filename):
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products


# Route qui afficher les produits en fonction de la source et de l'id optionnel
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []  # Initialise une liste vide pour les produits
    error = None  # Initialise le message d'erreur à None

    # Vérifie la source et lit les données appropriées
    if source == "json":
        products = read_json_file('products.json')
    elif source == "csv":
        products = read_csv_file('products.csv')
    elif source == "sql":
        products = read_sql_data('products.db', product_id)
        if not products:
            error = "Product not found in the database."
    else:
        error = "Wrong source specified. Please use 'json', 'csv', or 'sql'."

    # Si un product_id est fourni, filtre les produits par id
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found with the provided ID."

    return render_template(
        'product_display.html', products=products, error=error)


# Fonction auxiliaire pour lire les données depuis une base de données SQLite
def read_sql_data(db_file, product_id=None):
    products = []
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        if product_id:
            cursor.execute(
              "SELECT id, name, category, price FROM Products WHERE id = ?", (
                    product_id,))
        else:
            cursor.execute(
                "SELECT id, name, category, price FROM Products")
        products = cursor.fetchall()
        connection.close()
    except sqlite3.Error as e:
        error_message = f"Error reading from SQLite database: {e}"
        print(error_message)
        return []

    return [
        {"id": id, "name": name, "category": category, "price": price}
        for id, name, category, price in products
    ]


# Démarre l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
