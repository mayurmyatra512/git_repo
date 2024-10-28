from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det, Sales_order, Sales_order_det, Godown_det, Godown
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update
from .sales_order_det import updateOrdState

godown_data = Blueprint('godown_data', __name__)

ma = Marshmallow(app)


class GodownSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'godown_name', 'godown_loc', 'godown_type')


godown_data_schema = GodownSchema()
godown_datas_schema = GodownSchema(many=True)


@godown_data.route('/godownData', methods=['GET'])
def godownData():
    # alldata = db.session.execute(
    #     db.select(Godown.godown_name, Godown.godown_type)).all()
    # res = godown_datas_schema.dump(alldata)
    alldata = db.session.scalars(
        db.select(Godown.godown_name)).all()

    print(alldata)

    return alldata


def godownId(name):
    id = db.session.scalar(
        db.select(Godown.id).where(Godown.godown_name == name))
    # print(id)
    return id
