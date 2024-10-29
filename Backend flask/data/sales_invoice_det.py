from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy.sql.functions import func
from sqlalchemy import update, delete, select
from.items_data import minusqtyupdate, addqtyupdate

sales_invoice_det = Blueprint('sales_invoice_det', __name__)

ma = Marshmallow(app)


class SalesInvoiceDetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'billno', 'item_id', 'hsn', 'godown_id', 'item_qty', 'rate_per_piece',
                  'taxlessvalue_per_item', 'tim1', 'tim2', 'tim3', 'tim4', 'tim5', 'tim6', 'tim7', 'tim8',
                  'table_state', 'user_id', 'hsn_desc', 'gst_percentage', 'cgst', 'sgst')


sales_invoice_det_schema = SalesInvoiceDetSchema()
sales_invoices_det_schema = SalesInvoiceDetSchema(many=True)


def invoiceIDUpdate(billno, state):
    all_data = Sales_invoice_det.query.filter_by(table_state=state).all()

    # db.session.execute()


def updateState(billno, user_id):

    all_data = Sales_invoice_det.query.filter_by(
        user_id=user_id, table_state=1).update(dict(billno=billno, table_state=0))

    db.session.commit()
    return sales_invoice_det_schema.jsonify(all_data)


# ============================================DELETE All Sales Invoice Det Ledgers==============================================================================


@sales_invoice_det.route('/reloadSalesInvoice/<user_id>', methods=['DELETE'])
def reloadSalesInvoice(user_id):
    print(user_id)
    alldata = Sales_invoice_det.query.filter_by(
        table_state=1, user_id=user_id).all()

    res = sales_invoices_det_schema.dump(alldata)

    for x in res:
        print(x['item_qty'])
        addqtyupdate(id=x['item_id'], qty=x['item_qty'])

    all_data = Sales_invoice_det.query.filter_by(
        table_state=1, user_id=user_id).delete()

    db.session.commit()
    return sales_invoice_det_schema.jsonify(res)

# ============================================Add Sales Invoice Det Ledgers==============================================================================


@sales_invoice_det.route('/invoiceitemdet', methods=['POST'])
def invoiceitemdet():
    alter_id = (db.session.query(Sales_invoice_det.alter_id).count()) + 1
    item_id = request.json['item_id']
    hsn = request.json['hsn']
    godown_id = request.json['godown_id']
    item_qty = request.json['item_qty']
    rate_per_piece = request.json['rate_per_piece']
    taxlessvalue_per_item = request.json['taxlessvalue_per_item']
    user_id = request.json['user_id']
    hsn_desc = request.json['hsn_desc']
    gst_percentage = request.json['gst_percentage']
    cgst = request.json['cgst']
    sgst = request.json['sgst']
    # tim1 = request.json['tim1']
    # tim2 = request.json['tim2']
    # tim3 = request.json['tim3']
    # tim4 = request.json['tim4']
    # tim5 = request.json['tim5']
    # tim6 = request.json['tim6']
    # tim7 = request.json['tim7']
    # tim8 = request.json['tim8']

    my_data = Sales_invoice_det(alter_id=alter_id, item_id=item_id, hsn=hsn, godown_id=godown_id, item_qty=item_qty, rate_per_piece=rate_per_piece,
                                taxlessvalue_per_item=taxlessvalue_per_item, user_id=user_id, hsn_desc=hsn_desc, gst_percentage=gst_percentage, cgst=cgst, sgst=sgst)

    db.session.add(my_data)
    db.session.commit()

    res = minusqtyupdate(
        id=request.json['item_id'], qty=request.json['item_qty'])

    if res:
        return sales_invoice_det_schema.jsonify(my_data)
    else:
        return "Something is wrong"

# ============================================Edit Sales Invoice Det Ledgers==============================================================================


@sales_invoice_det.route("/invoiceitemupdate/<id>", methods=['PUT'])
def invoiceitemupdate(id):
    sale_inv_det = Sales_invoice_det.query.get(id)

    addqtyupdate(
        id=sale_inv_det.item_id, qty=sale_inv_det.item_qty)

    minusqtyupdate(
        id=request.json['item_id'], qty=request.json['item_qty'])

    alter_id = (db.session.query(
        Sales_invoice_det.alter_id).count()) + 1
    item_id = request.json['item_id']
    hsn = request.json['hsn']
    godown_id = request.json['godown_id']
    item_qty = request.json['item_qty']
    rate_per_piece = request.json['rate_per_piece']
    taxlessvalue_per_item = request.json['taxlessvalue_per_item']
    user_id = request.json['user_id']
    hsn_desc = request.json['hsn_desc']
    gst_percentage = request.json['gst_percentage']
    cgst = request.json['cgst']
    sgst = request.json['sgst']

    sale_inv_det.alter_id = alter_id
    sale_inv_det.item_id = item_id
    sale_inv_det.hsn = hsn
    sale_inv_det.godown_id = godown_id
    sale_inv_det.item_qty = item_qty
    sale_inv_det.rate_per_piece = rate_per_piece
    sale_inv_det.taxlessvalue_per_item = taxlessvalue_per_item
    sale_inv_det.user_id = user_id
    sale_inv_det.hsn_desc = hsn_desc
    sale_inv_det.gst_percentage = gst_percentage
    sale_inv_det.cgst = cgst
    sale_inv_det.sgst = sgst

    db.session.commit()
    return sales_invoice_det_schema.jsonify(sale_inv_det)

# ============================================Delete Sales Invoice Det Ledgers==============================================================================


@sales_invoice_det.route('/invoiceitemdelete/<id>', methods=['DELETE'])
def invoiceitemdelete(id):
    salesItem = Sales_invoice_det.query.get(id)
    db.session.delete(salesItem)
    db.session.commit()
    return sales_invoice_det_schema.jsonify(salesItem)

# ============================================Get Sales Invoice Det by state ==============================================================================


@sales_invoice_det.route('/sales_inv_item_det/<id>', methods=['GET'])
def sales_inv_item_det(id):
    inv_det_data = Sales_invoice_det.query.get(id)

    # res = addqtyupdate(id=inv_det_data.item_id, qty=inv_det_data.item_qty)

    return sales_invoice_det_schema.jsonify(inv_det_data)

# ============================================Get Sales Invoice Det by state ==============================================================================


@sales_invoice_det.route('/sales_inv_data', methods=['GET'])
def sales_inv_data():
    all_data = Sales_invoice_det.query.filter_by(table_state=1).all()
    res = sales_invoices_det_schema.dump(all_data)
    print(res)
    return jsonify(res)

# /invoiceitemdet
