from database import db
import uuid

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from dotenv import load_dotenv

load_dotenv()

#Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    name = db.Column(db.String(120))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    points = db.Column(db.Float(10,2))
    password_hash = db.Column(db.String(120))

    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password = password

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False) 
    price = db.Column(db.Float(10,2), unique=False, nullable=False)

class Voucher(db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
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