from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det, Sales_order, Sales_order_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update
from .sales_order_det import updateOrdState


sales_order = Blueprint('sales_order', __name__)

ma = Marshmallow(app)


class SalesOrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'vch_type', 'orderno', 'orderdate', 'ledger_id', 'salesperson_name', 'tot_taxlessvalue', 'CGST', 'SGST', 'taxpaidvalue',
                  'created_on', 'modified_on', 'user_id', 't_1', 't_2', 't_3', 't_4', 't_5', 't_6', 't_7', 't_8', 't_9', 't_10', 'status_so')


sales_order_schema = SalesOrderSchema()
sales_orders_schema = SalesOrderSchema(many=True)


@sales_order.route('/salesorder', methods=['POST'])
def salesorder():

    alter_id = (db.session.query(Sales_order.alter_id).count()) + 1
    vch_type = request.json['vch_type']
    orderno = request.json['orderno']
    orderdate = request.json['orderdate']
    ledger_id = request.json['ledger_id']
    salesperson_name = request.json['salesperson_name']
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

    my_data = Sales_order(alter_id=alter_id, vch_type=vch_type, orderno=orderno, orderdate=orderdate, ledger_id=ledger_id, salesperson_name=salesperson_name, tot_taxlessvalue=tot_taxlessvalue, CGST=CGST, SGST=SGST,
                          taxpaidvalue=taxpaidvalue, user_id=user_id)

    db.session.add(my_data)
    db.session.commit()

    updateOrdState(orderno=request.json['orderno'], user_id=user_id)

    return sales_order_schema.jsonify(my_data)


@sales_order.route('/orderno', methods=['GET'])
def orderno():
    res = db.session.query(func.max(Sales_order.orderno)).scalar()

    return jsonify(res)


@sales_order.route('/ordernolist', methods=['GET'])
def ordernolist():
    res = db.session.scalars(
        db.select(Sales_order.orderno)).all()

    return res


@sales_order.route('/sales_order_data_for_chalan/<data>', methods=['GET'])
def sales_order_data_for_chalan(data):
    print(data)

    alldata = db.session.scalars(
        db.select(Sales_order).where(Sales_order.orderno == data and Sales_order.status_so == 'Placed')).all()
    res = sales_orders_schema.dump(alldata)

    print(alldata)
    return sales_orders_schema.jsonify(res)
