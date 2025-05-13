from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()

def update_old_fields():
    products_ref = db.collection('products')
    docs = products_ref.stream()

    for doc in docs:
        data = doc.to_dict()
        updates = {}

        # Rename quantity -> available_stock
        if 'quantity' in data:
            updates['available_stock'] = data['quantity']
            updates['quantity'] = firestore.DELETE_FIELD

        # Rename limit -> minimum_stock_required
        if 'limit' in data:
            updates['minimum_stock_required'] = data['limit']
            updates['limit'] = firestore.DELETE_FIELD

        if updates:
            print(f"Updating document {doc.id} with {updates}")
            products_ref.document(doc.id).update(updates)

update_old_fields()
