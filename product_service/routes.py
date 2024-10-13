from flask import Blueprint, request, jsonify
from models import Book, db

book_blueprint = Blueprint('book_blueprint', __name__)

# Route to create a new book
@book_blueprint.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_year=data['published_year']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully!'}), 201

# Route to retrieve all books
@book_blueprint.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([
        {'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year}
        for book in books
    ])

@book_blueprint.route('/books/<int:book_id>', methods=['GET'])
def get_product_by_id(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_year': book.published_year
        }), 200
    else:
        return jsonify({'message': 'Product not found'}), 404