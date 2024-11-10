from flask import Flask, render_template
import json
import csv
import sqlite3


app = Flask(__name__)


def read_json_data():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading products.json: {e}")
        return []


def read_csv_data():
    products = []
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    except FileNotFoundError as e:
        print(f"Error loading products.csv: {e}")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    return products


def read_sql_data():
    products = []
    try:
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
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


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading items: {e}")
        items_list = []

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == "json":
        products = read_json_data()
    elif source == "csv":
        products = read_csv_data()
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