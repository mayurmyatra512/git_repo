from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Purchase_order, Purchase_order_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy.sql.functions import func
from sqlalchemy import update, delete, select, text
from.items_data import minusqtyupdate, addqtyupdate

pur_order_det = Blueprint('pur_order_det', __name__)

ma = Marshmallow(app)


class PurchaseOrderDetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'purorderno', 'item_id', 'hsn', 'godown_id', 'item_qty', 'rate_per_piece',
                  'taxlessvalue_per_item', 'tim1', 'tim2', 'tim3', 'tim4', 'tim5', 'tim6', 'tim7', 'tim8',
                  'table_state', 'user_id', 'hsn_desc', 'gst_percentage', 'cgst', 'sgst','status_so', 'prov_qty', 'pend_qty')


pur_order_det_schema = PurchaseOrderDetSchema()
pur_orders_det_schema = PurchaseOrderDetSchema(many=True)


def updateOrdState(orderno, user_id):

    all_data = Purchase_order_det.query.filter_by(
        user_id=user_id, table_state=1).update(dict(purorderno=orderno, table_state=0))

    db.session.commit()
    return pur_order_det_schema.jsonify(all_data)


# ============================================Get Sales Order Det by state ==============================================================================


@pur_order_det.route('/pur_ord_data', methods=['GET'])
def pur_ord_data():
    all_data = Purchase_order_det.query.filter_by(table_state=1).all()
    res = pur_orders_det_schema.dump(all_data)
    print(res)
    return jsonify(res)


# ============================================DELETE All Sales Order Det Ledgers==============================================================================


@pur_order_det.route('/reloadPurorder/<user_id>', methods=['DELETE'])
def reloadPurorder(user_id):
    print(user_id)
    alldata = Purchase_order_det.query.filter_by(
        table_state=1, user_id=user_id).all()

    res = pur_orders_det_schema.dump(alldata)

    # for x in res:
    #     print(x['item_qty'])
    #     addqtyupdate(id=x['item_id'], qty=x['item_qty'])

    all_data = Purchase_order_det.query.filter_by(
        table_state=1, user_id=user_id).delete()

    db.session.commit()
    return pur_orders_det_schema.jsonify(res)

# ============================================Add Sales Order Det Ledgers==============================================================================


@pur_order_det.route('/purorderitemdet', methods=['POST'])
def purorderitemdet():
    alter_id = (db.session.query(Purchase_order_det.alter_id).count()) + 1
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

    my_data = Purchase_order_det(alter_id=alter_id, item_id=item_id, hsn=hsn, godown_id=godown_id, item_qty=item_qty, rate_per_piece=rate_per_piece,
                              taxlessvalue_per_item=taxlessvalue_per_item, user_id=user_id, hsn_desc=hsn_desc, gst_percentage=gst_percentage, cgst=cgst, sgst=sgst)

    db.session.add(my_data)
    db.session.commit()

    # res = minusqtyupdate(
    #     id=request.json['item_id'], qty=request.json['item_qty'])

    # if res:
    return pur_order_det_schema.jsonify(my_data)
    # else:
    #     return "Something is wrong"

# ============================================Edit Sales Order Det Ledgers==============================================================================


@pur_order_det.route("/purorderitemupdate/<id>", methods=['PUT'])
def purorderitemupdate(id):
    pur_ord_det = Purchase_order_det.query.get(id)

    addqtyupdate(
        id=pur_ord_det.item_id, qty=pur_ord_det.item_qty)

    minusqtyupdate(
        id=request.json['item_id'], qty=request.json['item_qty'])

    alter_id = (db.session.query(
        Purchase_order_det.alter_id).count()) + 1
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
    pur_ord_det.alter_id = alter_id
    pur_ord_det.item_id = item_id
    pur_ord_det.hsn = hsn
    pur_ord_det.godown_id = godown_id
    pur_ord_det.item_qty = item_qty
    pur_ord_det.rate_per_piece = rate_per_piece
    pur_ord_det.taxlessvalue_per_item = taxlessvalue_per_item
    pur_ord_det.user_id = user_id
    pur_ord_det.hsn_desc = hsn_desc
    pur_ord_det.gst_percentage = gst_percentage
    pur_ord_det.cgst = cgst
    pur_ord_det.sgst = sgst

    db.session.commit()
    return pur_order_det_schema.jsonify(pur_ord_det)

# ============================================Delete Sales Order Det Ledgers==============================================================================


@pur_order_det.route('/purorderitemdelete/<id>', methods=['DELETE'])
def purorderitemdelete(id):
    purItem = Purchase_order_det.query.get(id)
    db.session.delete(purItem)
    db.session.commit()
    return pur_order_det_schema.jsonify(purItem)

# ============================================Get Sales Order Det by state ==============================================================================


@pur_order_det.route('/pur_ord_item_det/<id>', methods=['GET'])
def pur_ord_item_det(id):
    inv_det_data = Purchase_order_det.query.get(id)

    # res = addqtyupdate(id=inv_det_data.item_id, qty=inv_det_data.item_qty)

    return pur_order_det_schema.jsonify(inv_det_data)


@pur_order_det.route('pur_order_det_data_for_chalan/<data>', methods=['GET'])
def pur_order_det_data_for_chalan(data):
    # alldata = db.session.execute(
    #     db.select(Sales_order_det.id, Sales_order_det.orderno, Sales_order_det.item_id, Sales_order_det.item_qty, Sales_order_det.rate_per_piece,
    #               Sales_order_det.taxlessvalue_per_item, Sales_order_det.hsn, Sales_order_det.gst_percentage,
    #               Sales_order_det.cgst, Sales_order_det.sgst).where(Sales_order_det.orderno == data and Sales_order_det.status_so == 'Placed')).all()

    alldata = Purchase_order_det.query.filter_by(
        orderno=data, status_so='Placed').all()
    # alldata = Sales_order_det.query.filter_by(
    #     orderno=data, status_so='Placed').all()
    res = pur_orders_det_schema.dump(alldata)

    print(alldata)
    return pur_orders_det_schema.jsonify(res)

# def updatestatus(status):
#     db.session.scalars()



def updatepodetqty(orderno, prov_qty, pend_qty, item_id):
    # print(prov_qty)
    all_data = Purchase_order_det.query.filter_by(item_id=item_id, purorderno=orderno, status_so='Placed').update(dict(prov_qty=prov_qty, pend_qty=pend_qty))

    db.session.commit()
    return pur_order_det_schema.jsonify(all_data)