import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


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
        data = []

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


# Route to display products based on source and optional id
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filter by id if provided
    if product_id is not None:
        products = [product for product in products
                    if product['id'] == product_id]
        if not products:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
