import os
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)

from resources import VoucherByUserIdResource, CartByUserIdResource, ProductResource, ProductByProductIdResource, VoucherByVoucherIdResource, CartByCartIdResource

api.add_resource(VoucherByUserIdResource, '/vouchers/<string:user_id>', endpoint='voucherlist')
api.add_resource(VoucherByVoucherIdResource, '/voucher/<string:id>', endpoint='voucher')
api.add_resource(CartByUserIdResource, '/carts/<string:user_id>', endpoint='cartlist')
api.add_resource(CartByCartIdResource, '/cart/<string:id>', endpoint='cart')
api.add_resource(ProductByProductIdResource, '/product/<string:id>', endpoint='product')
api.add_resource(ProductResource, '/products', endpoint='productlist')
# api.add_resource(ParkLogByCardIdResource, '/parklog/<string:cardid>', endpoint='parklogid')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)