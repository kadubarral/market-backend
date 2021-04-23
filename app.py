import os
from flask import Flask
from database import db
from api import api, ns_product, ns_cart, ns_voucher, ns_user
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api.init_app(app)

from endpoints.resources import *

ns_user.add_resource(UserResource, "/")
ns_user.add_resource(UserbyUserUUIDResource, '/<string:uuid>', endpoint='user')
ns_voucher.add_resource(VoucherByUserIdResource, '/<string:user_uuid>', endpoint='voucherlist')
ns_voucher.add_resource(VoucherByVoucherCodeResource, '/code/<string:code>', endpoint='voucher')
ns_cart.add_resource(CartByUserIdResource, '/<string:user_uuid>', endpoint='cartlist')
ns_cart.add_resource(CartByCartIdResource, '/<string:id>', endpoint='cart')
ns_product.add_resource(ProductByProductIdResource, '/<string:uuid>', endpoint='product')
ns_product.add_resource(ProductResource, '/', endpoint='productlist')
ns_cart.add_resource(CartItemsByCartIdResource, '/items/<string:cart_id>', endpoint='cartitemlist')
ns_cart.add_resource(CartItemsByCartItemIdResource, '/items/<string:id>', endpoint='cartitem')
ns_cart.add_resource(CartSummaryByUserIdResource, '/summary/<string:user_uuid>', endpoint='cartsummary')
ns_cart.add_resource(CartDetailByCartIdResource, '/detail/<string:cart_id>', endpoint='cartdetail')
ns_cart.add_resource(CartResource, '/', endpoint='new_cart')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)