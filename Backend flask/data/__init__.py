from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()
userschema = {}
app = Flask(__name__)


def create_app():

    app.config['SECRET_KEY'] = 'jsdcjsdbcj sdcsdcsd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Magenta_1991@localhost/omitechworld'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app, supports_credentials=True)

    db.init_app(app)

    from .views import views
    from .ledgers_data import ledgers_data
    from .items_data import items_data
    from .sales_invoice_det import sales_invoice_det
    from .sales_data import sales_data
    from .purchase_invoice_det import purchase_invoice_det
    from .purchase_data import purchase_data
    from .pur_order import pur_order
    from .pur_order_det import pur_order_det
    from .sales_order import sales_order
    from .sales_order_det import sales_order_det
    from .issuedchalan_to_party import issuedchalan_to_party
    from .issuedchalan_det import issuedchalan_det
    from .godown_data import godown_data
    from .helper import helper

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(ledgers_data, url_prefix='/')
    app.register_blueprint(items_data, url_prefix='/')
    app.register_blueprint(sales_data, url_prefix='/')
    app.register_blueprint(sales_invoice_det, url_prefix='/')
    app.register_blueprint(purchase_data, url_prefix='/')
    app.register_blueprint(purchase_invoice_det, url_prefix='/')
    app.register_blueprint(pur_order, url_prefix='/')
    app.register_blueprint(pur_order_det, url_prefix='/')
    app.register_blueprint(sales_order, url_prefix='/')
    app.register_blueprint(sales_order_det, url_prefix='/')
    app.register_blueprint(issuedchalan_to_party, url_prefix='/')
    app.register_blueprint(issuedchalan_det, url_prefix='/')
    app.register_blueprint(godown_data, url_prefix='/')
    app.register_blueprint(helper, url_prefix='/')

    from .models import Ledger_master, Item_master, Ledger_groups, Item_groups, Sales_invoice_det, Sales_invoice, Sales_order, Sales_order_det, Transporter, Transporter_det, Issuedchalan, Issuedchalan_det, Godown, Godown_det, Purchase_order, Purchase_order_det, Purchase_invoice, Purchase_invoice_det

    with app.app_context():
        db.create_all()

    return app
