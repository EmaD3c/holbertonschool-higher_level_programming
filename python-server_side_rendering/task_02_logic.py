import json
from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
