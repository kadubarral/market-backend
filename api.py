from flask_restx import Api
api = Api()

ns_product = api.namespace('product', description='Product operations')
ns_voucher = api.namespace('voucher', description='Voucher operations')
ns_cart = api.namespace('cart', description='Cart operations')