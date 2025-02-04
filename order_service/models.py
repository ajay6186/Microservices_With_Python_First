from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='open')  # 'open' or 'checkout'

    def __repr__(self):
        return f"<Order {self.product_name}>"
