from flask import Blueprint, request, jsonify
from models import Order, db
import requests

order_blueprint = Blueprint('order_blueprint', __name__)

# Route to create a new order
@order_blueprint.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        user_id=data['user_id'],
        product_name=data['product_name'],
        status='open'
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully!'}), 201

# Route to retrieve all orders
@order_blueprint.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([
        {'id': order.id, 'user_id': order.user_id, 'product_name': order.product_name, 'status': order.status}
        for order in orders
    ])

# Route to change the status of an order to 'checkout'
@order_blueprint.route('/orders/<int:order_id>/checkout', methods=['PUT'])
def checkout_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    order.status = 'checkout'
    db.session.commit()
    return jsonify({'message': 'Order checked out successfully'})

# Route to get user details from the User API
@order_blueprint.route('/orders/<int:order_id>/user', methods=['GET'])
def get_order_user(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
# http://localhost:5000/api/register
    try:
        # Use the 'user-service' hostname defined in Docker Compose
        response = requests.get(f'http://localhost:5000/api/users/{order.user_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return jsonify({'message': 'User not found'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

