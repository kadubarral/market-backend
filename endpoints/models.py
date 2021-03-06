from database import db
import uuid

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from dotenv import load_dotenv

load_dotenv()

#Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120))
    username = db.Column(db.String(50), unique=True)
    points = db.Column(db.Float(10,2))
    userPublicKey = db.Column(db.String(500))
    cardNumber = db.Column(db.String(50))
    cardExpirationDate = db.Column(db.Date)
    cardCvv = db.Column(db.String(3))

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
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(50), unique=False, nullable=False) 
    price = db.Column(db.Float(10,2), unique=False, nullable=False)

class Voucher(db.Model):
    __tablename__ = 'vouchers'
    code = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('users.uuid'))
    discount = db.Column(db.Float)
    used = db.Column(db.Boolean, default=False)
    added_on = db.Column(TIMESTAMP, default=db.func.current_timestamp())

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    user_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('users.uuid'))
    voucher_code = db.Column(UUID(as_uuid=True), db.ForeignKey('vouchers.code'), nullable=True)
    added_on = db.Column(TIMESTAMP, default=db.func.current_timestamp())

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    product_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('products.uuid'))