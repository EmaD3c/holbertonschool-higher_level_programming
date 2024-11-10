import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')


# Route pour la page 'about'
@app.route('/about')
def about():
    return render_template('about.html')


# Route pour la page 'contact'
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Route pour afficher les éléments à partir d'un fichier JSON
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_data = data.get("items", [])
    except FileNotFoundError:
        item_data = []

    return render_template('items.html', items=item_data)


# Route pour afficher les produits
@app.route('/products', methods=['GET'])
def display_products():
    source = request.args.get('source', '')
    product_id = request.args.get('id', type=int)
    message = None
    products = []

    # Vérification de la source
    if source not in ['json', 'csv', 'sql']:
        message = "Wrong source"
        return render_template(
            'product_display.html', products=products, message=message)

    try:
        # Si la source est JSON
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)

        # Si la source est CSV
        elif source == 'csv':
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]

        # Si la source est SQL (SQLite)
        elif source == 'sql':
            con = sqlite3.connect("products.db")
            cur = con.cursor()

            if product_id:
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

        # Si un id a été fourni filtrer les produits pour correspondre à cet id
        if product_id:
            products = [
                product for product in products if product['id'] == product_id
                ]
            if not products:
                message = "Product not found."

    except FileNotFoundError:
        message = "File not found."
    except sqlite3.Error as e:
        message = f"Database error: {e}"
    except Exception as e:
        message = f"An error occurred: {e}"

    # Rendu de la page avec les produits ou les messages d'erreur
    return render_template(
        'product_display.html', products=products, message=message)


# Fonction principale pour démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
