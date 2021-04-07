import os

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password_hash = Column(String(120))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False, nullable=False) 
    price = Column(Float(10,2), unique=False, nullable=False)

class Voucher(Base):
    __tablename__ = 'vouchers'
    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    discount = Column(Integer)
    added_on = Column(TIMESTAMP, default=func.current_timestamp())

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    voucher_id = Column(Integer, ForeignKey('vouchers.id'), nullable=True)
    added_on = Column(TIMESTAMP, default=func.current_timestamp())

class CartItem(Base):
    __tablename__ = 'cart_item'
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
 
if __name__ == "__main__":
    from sqlalchemy import create_engine
    engine = create_engine(os.environ['DATABASE_URL'])
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)