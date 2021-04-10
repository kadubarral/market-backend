from endpoints.models import CartItem, User, Cart, Voucher, Product
from database import db
from sqlalchemy import func
from api import ns_product

from flask_restx import abort
from flask_restx import fields, Resource, marshal_with, reqparse

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'uri': fields.Url('user', absolute=True),
}

product_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'price': fields.Float,
    'uri': fields.Url('product', absolute=True),
}

voucher_fields = {
    'id': fields.Integer,
    'code': fields.String,
    'user_id': fields.Integer,
    'discount': fields.Float,
    'added_on': fields.DateTime(dt_format='rfc822'),
    'uri': fields.Url('voucher', absolute=True),
}

cart_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'voucher_id': fields.Integer,
    'added_on': fields.DateTime(dt_format='rfc822'),
    'uri': fields.Url('cart', absolute=True),
}

cartItem_fields = {
    'id': fields.Integer,
    'cart_id': fields.Integer,
    'product_id': fields.Integer,
    'uri': fields.Url('cartitem', absolute=True),
}


cartsummary_fields = {
    'id': fields.Integer,
    'added_on': fields.DateTime(dt_format='rfc822'),
    'discount': fields.Float,
    'total': fields.Float,
}

cartdetail_fields = {
    'title': fields.String,
    'price': fields.Float,
}

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('price', type=float)

class ProductResource(Resource):
    @marshal_with(product_fields, "data")
    def get(self):
        productlist = db.session.query(Product).all()
        return productlist

    @ns_product.expect(parser)
    def post(self):
        parsed_args = parser.parse_args()
        new_product = Product(title = parsed_args['title'], 
                                price = parsed_args['price'])

        db.session.add(new_product)
        db.session.commit()

        return 201

class ProductByProductIdResource(Resource):
    @marshal_with(product_fields, "data")
    def get(self, id):
        product = db.session.query(Product).filter(Product.id == id).all()
        if not product:
            abort(404, message="Product {} doesn't exist".format(id))
        return product

class VoucherByUserIdResource(Resource):
    @marshal_with(voucher_fields, "data")
    def get(self, user_id):
        voucherlist = db.session.query(Voucher).filter(Voucher.user_id == user_id).all()
        if not voucherlist:
            abort(404, message="User {} doesn't have vouchers or doesn't exist".format(user_id))
        return voucherlist

class VoucherByVoucherIdResource(Resource):
    @marshal_with(voucher_fields, "data")
    def get(self, id):
        voucher = db.session.query(Voucher).filter(Voucher.id == id).all()
        if not voucher:
            abort(404, message="Voucher {} doesn't exist".format(id))
        return voucher

class CartByUserIdResource(Resource):
    @marshal_with(cart_fields, "data")
    def get(self, user_id):
        cartlist = db.session.query(Cart).filter(Cart.user_id == user_id).all()
        if not cartlist:
            abort(404, message="User {} doesn't have carts or doesn't exist".format(user_id))
        return cartlist

class CartByCartIdResource(Resource):
    @marshal_with(cart_fields, "data")
    def get(self, id):
        cart = db.session.query(Cart).filter(Cart.id == id).all()
        if not cart:
            abort(404, message="Cart {} doesn't exist".format(id))
        return cart

class CartItemsByCartIdResource(Resource):
    @marshal_with(cartItem_fields, "data")
    def get(self, cart_id):
        cartitemlist = db.session.query(CartItem).filter(CartItem.cart_id == cart_id).all()
        if not cartitemlist:
            abort(404, message="Cart {} doesn't have any item or doesn't exist".format(cart_id))
        return cartitemlist

class CartItemsByCartItemIdResource(Resource):
    @marshal_with(cartItem_fields, "data")
    def get(self, id):
        cartitem = db.session.query(CartItem).filter(CartItem.id == id).all()
        if not cartitem:
            abort(404, message="CartItem {} doesn't exist".format(id))
        return cartitem

class CartFullByUserIdResource(Resource):
    @marshal_with(cartItem_fields, "data")
    def get(self, id):
        cartitem = db.session.query(CartItem).filter(CartItem.id == id).all()
        if not cartitem:
            abort(404, message="CartItem {} doesn't exist".format(id))
        return cartitem

class CartSummaryByUserIdResource(Resource):
    @marshal_with(cartsummary_fields, "data")
    def get(self, user_id):
        cartsummary = db.session.query(Cart.id,
                                    Cart.added_on, 
                                    Voucher.discount,
                                    func.sum(Product.price * (100-func.coalesce(Voucher.discount,0))/100).label("total")) \
                .join(CartItem, Cart.id==CartItem.cart_id,) \
                .join(Product, CartItem.product_id==Product.id) \
                .outerjoin(Voucher, Cart.voucher_id==Voucher.id) \
                .filter(Cart.user_id == user_id) \
                .group_by(Cart.id, Cart.added_on, Voucher.discount) \
                .all()
        if not cartsummary:
            abort(404, message="Cart {} doesn't exist".format(id))
        return cartsummary

class CartDetailByCartIdResource(Resource):
    @marshal_with(cartdetail_fields, "data")
    def get(self, cart_id):
        cartdetail = db.session.query(Product.title,
                                    Product.price) \
                .join(CartItem, CartItem.product_id==Product.id) \
                .filter(CartItem.cart_id == cart_id) \
                .all()
        if not cartdetail:
            abort(404, message="Cart {} doesn't exist".format(id))
        return cartdetail

# class ParkLogResource(Resource):
#     @marshal_with(parklog_fields)
#     @marshal_with(parkstatus_fields)
#     def post(self):
#         parsed_args = parser.parse_args()
#         new_activity = ParkLog(activity = parsed_args['activity'], cardid = parsed_args['cardid'], parkid = parsed_args['parkid'])
        
#         db.session.add(new_activity)
        
#         parkstatus = db.session.query(ParkStatus).filter(ParkStatus.parkid == parsed_args['parkid']).first()
        
#         if parsed_args['activity'] == 'I':
#             parkstatus.available -= 1
#         elif parsed_args['activity'] == 'O':
#             parkstatus.available += 1
#         else:
#             abort(404, message="Activity values must be I (in) or O (out)")
        
#         db.session.add(parkstatus)
#         db.session.commit()

#         return parkstatus, 201