from flask import Blueprint, request, jsonify
from models import User, db

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@user_blueprint.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@user_blueprint.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# New route to get a specific user by user_id
@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    else:
        return jsonify({'message': 'User not found'}), 404