import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# Routes for static pages
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# The /items route reads the JSON file items.
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            # parses the contents of the items.json
            # converts it from JSON format into a Python dictionary.
            data = json.load(f)
            # extracts the value
            item_data = data.get("items")
    except FileNotFoundError:
        item_data = []

    return render_template('items.html', items=item_data)


# Helper function to read JSON data
def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Helper function to read CSV data
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


# Helper function to read data from SQLite database
def read_sql_data(filename):
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
        print(f"Database error: {e}")
    return products


# Route to display products based on source and optional id
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == "json":
        products = read_json_file()
    elif source == "csv":
        products = read_csv_file()
    else:
        error = "Wrong source specified. Please use 'json' or 'csv'."
        return render_template('product_display.html', error=error)

    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            error = "Product not found."

    return render_template(
        'product_display.html', products=products, error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
