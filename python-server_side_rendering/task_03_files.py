import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def load_products_from_json():
    """
    Load products.json whether it’s a top‐level list or wrapped in a dict.
    Returns list of dicts, or None on read/parse error.
    """
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
    except Exception:
        return None

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        if 'products' in data and isinstance(data['products'], list):
            return data['products']
        for val in data.values():
            if isinstance(val, list):
                return val

    return []

def load_products_from_csv():
    """
    Read products.csv via csv.DictReader.
    Returns list of dicts, or None on error.
    """
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = []
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                except:
                    pass
                try:
                    row['price'] = float(row['price'])
                except:
                    pass
                products.append(row)
        return products
    except Exception:
        return None

@app.route('/products')
def products():
    source   = request.args.get('source')
    id_param = request.args.get('id')

    error = None
    products_list = []

    if source == 'json':
        products_list = load_products_from_json()
        if products_list is None:
            error = 'Error reading JSON file'
    elif source == 'csv':
        products_list = load_products_from_csv()
        if products_list is None:
            error = 'Error reading CSV file'
    else:
        error = 'Wrong source'

    if not error and id_param:
        try:
            target_id = int(id_param)
            filtered = [p for p in products_list if p.get('id') == target_id]
            if filtered:
                products_list = filtered
            else:
                error = 'Product not found'
        except:
            error = 'Product not found'

    return render_template(
        'product_display.html',
        products=products_list,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
