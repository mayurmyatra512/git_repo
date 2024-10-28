from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Purchase_invoice, Purchase_invoice_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update
from .purchase_invoice_det import updateState


purchase_data = Blueprint('purchase_data', __name__)

ma = Marshmallow(app)

class PurchaseInoiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'vch_type', 'billno', 'billdate', 'ledger_id', 'discountvalue', 'tot_taxlessvalue', 'CGST', 'SGST', 'taxpaidvalue',
                  'narration', 'amt_paid', 'overdue', 'outstanding_id', 'created_on', 'modified_on', 'ost_mod_on', 'user_id', 't_1', 't_2', 't_3', 't_4', 't_5', 't_6', 't_7', 't_8', 't_9', 't_10', 'chalantype', 'chalanno', 'so_no')



purchase_invoice_schema = PurchaseInoiceSchema()
purchase_invoices_schema = PurchaseInoiceSchema(many=True)


@purchase_data.route('/purchaseinvoice', methods=['POST'])
def purchaseinvoice():

    alter_id = (db.session.query(Purchase_invoice.alter_id).count()) + 1
    vch_type = request.json['vch_type']
    billno = request.json['billno']
    billdate = request.json['billdate']
    ledger_id = request.json['ledger_id']
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

    my_data = Purchase_invoice(alter_id=alter_id, vch_type=vch_type, billno=billno, billdate=billdate, ledger_id=ledger_id, discountvalue=discountvalue, tot_taxlessvalue=tot_taxlessvalue, CGST=CGST, SGST=SGST,
                            taxpaidvalue=taxpaidvalue, narration=narration, amt_paid=amt_paid, overdue=overdue, outstanding_id=outstanding_id, user_id=user_id)

    db.session.add(my_data)
    db.session.commit()

    updateState(billno=request.json['billno'], user_id=user_id)

    return purchase_invoice_schema.jsonify(my_data)


@purchase_data.route('/purbillno', methods=['GET'])
def billno():
    res = db.session.query(func.max(Purchase_invoice.billno)).scalar()

    return jsonify(res)     
