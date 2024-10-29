from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update
from .sales_invoice_det import updateState


sales_data = Blueprint('sales_data', __name__)

ma = Marshmallow(app)


class SalesInoiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'vch_type', 'billno', 'billdate', 'ledger_id', 'salesperson_name', 'discountvalue', 'tot_taxlessvalue', 'CGST', 'SGST', 'taxpaidvalue',
                  'narration', 'amt_paid', 'overdue', 'outstanding_id', 'created_on', 'modified_on', 'ost_mod_on', 'user_id', 't_1', 't_2', 't_3', 't_4', 't_5', 't_6', 't_7', 't_8', 't_9', 't_10', 'chalantype', 'chalanno', 'so_no')


sales_invoice_schema = SalesInoiceSchema()
sales_invoices_schema = SalesInoiceSchema(many=True)


@sales_data.route('/salesinvoice', methods=['POST'])
def salesinvoice():

    alter_id = (db.session.query(Sales_invoice.alter_id).count()) + 1
    vch_type = request.json['vch_type']
    billno = request.json['billno']
    billdate = request.json['billdate']
    ledger_id = request.json['ledger_id']
    salesperson_name = request.json['salesperson_name']
    # item_det_id = request.json['item_det_id']
    discountvalue = request.json['discountvalue']
    tot_taxlessvalue = request.json['tot_taxlessvalue']
    CGST = request.json['CGST']
    SGST = request.json['SGST']
    # IGST = request.json['IGST']
    taxpaidvalue = request.json['taxpaidvalue']
    narration = request.json['narration']
    amt_paid = request.json['amt_paid']
    overdue = request.json['overdue']
    outstanding_id = request.json['outstanding_id']
    # created_on = request.json['created_on']
    # modified_on = request.json['modified_on']
    # ost_mod_on = request.json['ost_mod_on']
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

    my_data = Sales_invoice(alter_id=alter_id, vch_type=vch_type, billno=billno, billdate=billdate, ledger_id=ledger_id, salesperson_name=salesperson_name, discountvalue=discountvalue, tot_taxlessvalue=tot_taxlessvalue, CGST=CGST, SGST=SGST,
                            taxpaidvalue=taxpaidvalue, narration=narration, amt_paid=amt_paid, overdue=overdue, outstanding_id=outstanding_id, user_id=user_id)

    db.session.add(my_data)
    db.session.commit()

    updateState(billno=request.json['billno'], user_id=user_id)

    return sales_invoice_schema.jsonify(my_data)


@sales_data.route('/billno', methods=['GET'])
def billno():
    res = db.session.query(func.max(Sales_invoice.billno)).scalar()

    return jsonify(res)
