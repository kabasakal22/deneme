from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory product catalog
products = [
    {"id": 1, "name": "Product 1", "price": 10.0},
    {"id": 2, "name": "Product 2", "price": 20.0},
    {"id": 3, "name": "Product 3", "price": 30.0},
]

# Simple in-memory cart structure
cart = {}

@app.route('/products', methods=['GET'])
def list_products():
    """Return the list of available products."""
    return jsonify(products)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Add a product to the cart."""
    data = request.get_json(force=True)
    product_id = int(data.get('product_id'))
    quantity = int(data.get('quantity', 1))
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    cart[product_id] = cart.get(product_id, 0) + quantity
    return jsonify({'cart': cart}), 201

@app.route('/cart', methods=['GET'])
def get_cart():
    """Retrieve items currently in the cart."""
    items = []
    for pid, qty in cart.items():
        product = next((p for p in products if p['id'] == pid), None)
        if product:
            items.append({'product': product, 'quantity': qty})
    return jsonify(items)

@app.route('/checkout', methods=['POST'])
def checkout():
    """Simulate a checkout operation and clear the cart."""
    total = 0.0
    for pid, qty in cart.items():
        product = next((p for p in products if p['id'] == pid), None)
        if product:
            total += product['price'] * qty
    cart.clear()
    return jsonify({'total': total})

if __name__ == '__main__':
    # Development server
    app.run(debug=True)
