import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/products')
def products():
    source   = request.args.get('source')
    id_param = request.args.get('id')

    products_list = []
    error = None

    if source not in ('json', 'csv'):
        error = 'Wrong source'
    else:
        if source == 'json':
            try:
                f = open('products.json', 'r')
                data = json.load(f)
                f.close()
                products_list = data.get('products', [])
            except:
                error = 'Error reading JSON file'

        else:
            try:
                f = open('products.csv', 'r')
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        row['id']    = int(row['id'])
                        row['price'] = float(row['price'])
                    except:
                        pass
                    products_list.append(row)
                f.close()
            except:
                error = 'Error reading CSV file'

    if error is None and id_param:
        try:
            target_id = int(id_param)
        except:
            error = 'Product not found'
        else:
            found = [p for p in products_list if p.get('id') == target_id]
            if not found:
                error = 'Product not found'
            else:
                products_list = found

    return render_template(
        'product_display.html',
        products=products_list,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
