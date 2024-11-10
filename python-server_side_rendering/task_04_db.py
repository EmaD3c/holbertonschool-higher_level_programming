import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')


# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')


# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# The /items route reads the JSON file items
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_data = data.get("items", [])
    except FileNotFoundError:
        item_data = []

    return render_template('items.html', items=item_data)


# Helper function to read JSON data from a file
def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Helper function to read CSV data from a file
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


# Route to display products based on the source and optional id
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)  # Get product ID if provided
    products = []  # Initialize an empty list for products
    error = None  # Initialize error message as None

    # Check the source and read the appropriate data
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

    # If product_id is provided, filter products by id
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found with the provided ID."

    return render_template(
        'product_display.html', products=products, error=error)


# Helper function to read data from SQLite database
def read_sql_data(filename, product_id=None):
    products = []
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        if product_id:
            cursor.execute(
              "SELECT id, name, category, price FROM Products WHERE id = ?", (
                    product_id,))
        else:
            cursor.execute(
                "SELECT id, name, category, price FROM Products")
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
        print(f"Database error: {e}")
    return products


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
