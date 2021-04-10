from database import db

from sqlalchemy.sql.sqltypes import TIMESTAMP
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

#Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(120))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False) 
    price = db.Column(db.Float(10,2), unique=False, nullable=False)

class Voucher(db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    discount = db.Column(db.Float)
    added_on = db.Column(TIMESTAMP, default=db.func.current_timestamp())

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    voucher_id = db.Column(db.Integer, db.ForeignKey('vouchers.id'), nullable=True)
    added_on = db.Column(TIMESTAMP, default=db.func.current_timestamp())

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
 
# if __name__ == "__main__":
#     from sqlalchemy import create_engine
#     engine = create_engine(os.environ['DATABASE_URL'])
#     db.Model.metadata.drop_all(engine)
#     db.Model.metadata.create_all(engine)