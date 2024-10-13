from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import user_blueprint
from models import db

app = Flask(__name__)
from flask_cors import CORS
CORS(app) 
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# Register the blueprint
app.register_blueprint(user_blueprint, url_prefix='/api')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
