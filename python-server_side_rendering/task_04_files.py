import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def load_json():
    try:
        with open('products.json') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'products' in data:
            return data['products']
        if isinstance(data, list):
            return data
        for v in data.values():
            if isinstance(v, list):
                return v
        return []
    except:
        return None

def load_csv():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            rows = []
            for r in reader:
                try:
                    r['id'] = int(r['id'])
                    r['price'] = float(r['price'])
                except:
                    pass
                rows.append(r)
            return rows
    except:
        return None

def load_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
    except:
        return None

@app.route('/products')
def products():
    source   = request.args.get('source')
    id_param = request.args.get('id')

    error = None
    products_list = None

    if source == 'json':
        products_list = load_json()
        if products_list is None:
            error = 'Error reading JSON file'
    elif source == 'csv':
        products_list = load_csv()
        if products_list is None:
            error = 'Error reading CSV file'
    elif source == 'sql':
        products_list = load_sql()
        if products_list is None:
            error = 'Error reading SQLite database'
    else:
        error = 'Wrong source'

    if not error and id_param:
        try:
            target = int(id_param)
            filtered = [p for p in products_list if p.get('id') == target]
            if filtered:
                products_list = filtered
            else:
                error = 'Product not found'
        except:
            error = 'Product not found'

    return render_template(
        'product_display.html',
        products=products_list or [],
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
