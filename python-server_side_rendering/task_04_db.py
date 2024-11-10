import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# Routes pour les pages statiques
@app.route('/')
def home():
    """Affiche la page d'accueil."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Affiche la page À propos."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Affiche la page Contact."""
    return render_template('contact.html')


# Route pour afficher les items à partir du fichier JSON
@app.route('/items')
def items():
    """Affiche les items à partir du fichier JSON `items.json`."""
    try:
        with open('items.json', 'r') as f:
            # Analyse le contenu du fichier JSON et extrait la liste des items
            data = json.load(f)
            item_data = data.get("items")
    except FileNotFoundError:
        item_data = []

    return render_template('items.html', items=item_data)


# Fonction pour lire les données JSON
def read_json_file(filename):
    """Lit et renvoie les données JSON du fichier spécifié."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Fonction pour lire les données CSV
def read_csv_file(filename):
    """Lit et renvoie les données CSV du fichier spécifié."""
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


# Fonction pour lire les données de la base de données SQLite
def read_sql_data(filename):
    """Lit et renvoie les données de la base de données SQLite spécifiée."""
    products = []
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Erreur de base de données : {e}")
    return products


# Route affiche les produits en fonction de la source et de l'id facultatif
@app.route('/products', methods=['GET'])
def display_products():
    """Affiche les produits en fonction de la source (JSON, CSV ou SQL)"""
    source = request.args.get('source', '')
    product_id = request.args.get('id', type=int)
    message = None
    products = []

    if source not in ['json', 'csv', 'sql']:
        message = "Source incorrecte"

    try:
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)

        elif source == 'csv':
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]

        elif source == 'sql':
            con = sqlite3.connect("products.db")
            cur = con.cursor()

            if product_id:
                print(
                  f"Exécution de la requête : SELECT * FROM Products WHERE "
                  f"id = {product_id}"
                )
                query = "SELECT * FROM Products WHERE id = ?"
                cur.execute(query, (product_id,))
            else:
                query = "SELECT * FROM Products"
                cur.execute(query)

            products = [
                {
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3]
                }
                for row in cur.fetchall()
            ]
            con.close()

            print(f"Produits récupérés : {products}")

        if product_id:
            products = [
                product for product in products if product['id'] == product_id
            ]
            print(f"Produits filtrés : {products}")
            if not products:
                message = "Produit non trouvé."

    except FileNotFoundError:
        message = "Fichier introuvable."

    except Exception as e:
        message = f"Une erreur est survenue : {e}"

    return render_template(
        'product_display.html', products=products, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
