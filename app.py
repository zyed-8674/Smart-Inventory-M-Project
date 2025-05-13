from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    products_ref = db.collection('products')
    products = []
    for doc in products_ref.stream():
        item = doc.to_dict()
        item['id'] = doc.id
        item['product_name'] = item.get('name', '')
        item['available_stock'] = item.get('available_stock', 0)
        item['minimum_stock_required'] = item.get('minimum_stock_required', 0)
        products.append(item)
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    product_name = request.form['product_name']
    available_stock = int(request.form['available_stock'])
    minimum_stock_required = int(request.form['minimum_stock_required'])

    db.collection('products').add({
        'name': product_name,
        'available_stock': available_stock,
        'minimum_stock_required': minimum_stock_required
    })
    return redirect('/')

@app.route('/delete/<product_id>', methods=['GET'])
def delete_product(product_id):
    db.collection('products').document(product_id).delete()
    return redirect('/')

@app.route('/edit/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product_ref = db.collection('products').document(product_id)
    
    if request.method == 'POST':
        product_name = request.form['product_name']
        available_stock = int(request.form['available_stock'])
        minimum_stock_required = int(request.form['minimum_stock_required'])

        product_ref.update({
            'name': product_name,
            'available_stock': available_stock,
            'minimum_stock_required': minimum_stock_required
        })
        return redirect('/')

    product = product_ref.get().to_dict()
    product['id'] = product_id
    return render_template('edit.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
