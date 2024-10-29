from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det, Purchase_order, Purchase_order_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update
from .pur_order_det import updateOrdState


pur_order = Blueprint('pur_order', __name__)

ma = Marshmallow(app)


class PurchaseOrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'vch_type', 'purorderno', 'purorderdate', 'ledger_id','tot_taxlessvalue', 'CGST', 'SGST', 'taxpaidvalue',
                  'created_on', 'modified_on', 'user_id', 't_1', 't_2', 't_3', 't_4', 't_5', 't_6', 't_7', 't_8', 't_9', 't_10', 'status_so')


purchase_order_schema = PurchaseOrderSchema()
purchase_orders_schema = PurchaseOrderSchema(many=True)


@pur_order.route('/purorder', methods=['POST'])
def purorder():

    alter_id = (db.session.query(Purchase_order.alter_id).count()) + 1
    vch_type = request.json['vch_type']
    orderno = request.json['orderno']
    orderdate = request.json['orderdate']
    ledger_id = request.json['ledger_id']
    # item_det_id = request.json['item_det_id']
    tot_taxlessvalue = request.json['tot_taxlessvalue']
    CGST = request.json['CGST']
    SGST = request.json['SGST']
    # IGST = request.json['IGST']
    taxpaidvalue = request.json['taxpaidvalue']
    # created_on = request.json['created_on']
    # modified_on = request.json['modified_on']
    user_id = request.json['user_id']
    # t_1 = request.json['t_1']
    # t_2 = request.json['t_2']
    # t_3 = request.json['t_3']
    # t_4 = request.json['t_4']
    # t_5 = request.json['t_5']
    # t_6 = request.json['t_6']
    # t_7 = request.json['t_7']
    # t_8 = request.json['t_8']
    # t_9 = request.json['t_9']
    # t_10 = request.json['t_10']

    my_data = Purchase_order(alter_id=alter_id, vch_type=vch_type, purorderno=orderno, purorderdate=orderdate, ledger_id=ledger_id, tot_taxlessvalue=tot_taxlessvalue, CGST=CGST, SGST=SGST,
                          taxpaidvalue=taxpaidvalue, user_id=user_id)

    db.session.add(my_data)
    db.session.commit()

    updateOrdState(orderno=request.json['orderno'], user_id=user_id)

    return purchase_order_schema.jsonify(my_data)


@pur_order.route('/purorderno', methods=['GET'])
def purorderno():
    res = db.session.query(func.max(Purchase_order.purorderno)).scalar()

    return jsonify(res)


@pur_order.route('/purordernolist', methods=['GET'])
def purordernolist():
    res = db.session.scalars(
        db.select(Purchase_order.purorderno)).all()

    return res


@pur_order.route('/purchase_order_data_for_chalan/<data>', methods=['GET'])
def purchase_order_data_for_chalan(data):
    print(data)

    alldata = db.session.scalars(
        db.select(Purchase_order).where(Purchase_order.purorderno == data and Purchase_order.status_so == 'Placed')).all()
    res = purchase_orders_schema.dump(alldata)

    print(alldata)
    return purchase_orders_schema.jsonify(res)
