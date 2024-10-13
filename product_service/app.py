from flask import Flask
from models import db
from routes import book_blueprint

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and register blueprint
db.init_app(app)
app.register_blueprint(book_blueprint, url_prefix='/api')

# Create database tables if not already present
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
