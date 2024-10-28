
from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det, Issuedchalan, Issuedchalan_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update, delete
# from .issuedchalan_det import updateOrdState
from sqlalchemy.sql import text
from .godown_data import godownId
from .items_data import minusqtyupdate, addqtyupdate, itemId
from .issuedchalan_to_party import postorderchalan
from .sales_order_det import updatesodetqty
from .pur_order_det import updatepodetqty


issuedchalan_det = Blueprint('issuedchalan_det', __name__)

ma = Marshmallow(app)


class IssuedChalanDetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'chalanno', 'item_id', 'hsn', 'godown_id', 'item_qty', 'rate_per_piece', 'taxlessvalue_per_item', 'tim1',
                  'tim2', 'tim3', 'tim4', 'tim5', 'tim6', 'tim7', 'tim8', 'table_state', 'user_id', 'hsn_desc', 'gst_percentage', 'cgst', 'sgst', 'orderno', 'prov_qty', 'pend_qty', 'status','voucher_type')


issuedchalan_det_schema = IssuedChalanDetSchema()
issuedchalans_det_schema = IssuedChalanDetSchema(many=True)


# ============================================Get Sales Order Det by state ==============================================================================

@issuedchalan_det.route('/sales_chalan_data', methods=['GET'])
def sales_chalan_data():
    all_data = Issuedchalan_det.query.filter_by(table_state=1, voucher_type=1).all()
    res = issuedchalans_det_schema.dump(all_data)
    print(res)
    return jsonify(res)


# ============================================DELETE All Sales Order Det Ledgers==============================================================================

@issuedchalan_det.route('/reloadSaleschalan/<user_id>', methods=['DELETE'])
def reloadSaleschalan(user_id):
    print(user_id)
    alldata = Issuedchalan_det.query.filter_by(
        table_state=1, user_id=user_id, voucher_type=1).all()

    res = issuedchalans_det_schema.dump(alldata)

    # for x in res:
    #     print(x['item_qty'])
    #     addqtyupdate(id=x['item_id'], qty=x['item_qty'])

    all_data = Issuedchalan_det.query.filter_by(
        table_state=1, user_id=user_id, voucher_type=1).delete()

    db.session.commit()
    return issuedchalan_det_schema.jsonify(res)


# ============================================Delete Sales Order Det Ledgers==============================================================================

@issuedchalan_det.route('/chalanitemdelete/<id>', methods=['DELETE'])
def chalanitemdelete(id):
    chalanItem = Issuedchalan_det.query.get(id)
    db.session.delete(chalanItem)
    db.session.commit()
    return issuedchalan_det_schema.jsonify(chalanItem)

# ============================================Get Sales Order Det by state ==============================================================================


@issuedchalan_det.route('/issuedchalan_item_det/<id>', methods=['GET'])
def issuedchalan_item_det(id):
    chalan_det_data = Issuedchalan_det.query.get(id)

    # res = addqtyupdate(id=inv_det_data.item_id, qty=inv_det_data.item_qty)

    return Issuedchalan_det.jsonify(chalan_det_data)

# ============================================Update Sales chalan ==============================================================================
@issuedchalan_det.route('/chalandetails', methods=['POST'])
def chalandetails():
    orderno = request.json['orderno']
    chalanno = request.json['chalanno']
    user_id = request.json['user_id']
    godown_id = request.json['godown_id']

    res = postorderchalan(orderno, chalanno, user_id, godown_id)
    return res


# ============================================Add Sales chalan Det ==============================================================================


@issuedchalan_det.route('/chalanitemdetails', methods=['POST'])
def chalanitemdetails():
    alter_id = (db.session.query(Issuedchalan_det.alter_id).count()) + 1

    hsn = request.json['hsn']
    name = request.json['godown_id']
    godown_id = godownId(name)
    item_qty = request.json['item_qty']
    rate_per_piece = request.json['rate_per_piece']
    taxlessvalue_per_item = request.json['taxlessvalue_per_item']
    user_id = request.json['user_id']
    hsn_desc = request.json['hsn_desc']
    gst_percentage = request.json['gst_percentage']
    cgst = request.json['cgst']
    sgst = request.json['sgst']
    orderno = request.json['orderno']
    vch_type = request.json['vch_type']
    status = request.json['status']
    
    if orderno != "":
        table_state = 0
        itid = request.json['item_id']
        item_id = itemId(itid)
        # chalanno = request.json['chalanno']
        prov_qty = request.json['prov_qty']
        pend_qty = request.json['pend_qty']
        if vch_type == "Sale chalan" | vch_type == "Purchase Return chalan":
            voucher_type = 1
            updatesodetqty(orderno, prov_qty, pend_qty, item_id)
            res = minusqtyupdate(id=item_id, qty=request.json['prov_qty'])

        elif vch_type == "Purchase chalan" | vch_type == "Sale Return chalan":
            voucher_type = 2
            updatepodetqty(orderno, prov_qty, pend_qty, item_id)
            res = addqtyupdate(id=item_id, qty=request.json['prov_qty'])
        # postorderchalan(orderno, chalanno, user_id, godown_id)
    else:
        table_state = 1
        prov_qty = request.json['item_qty']
        item_id = request.json['item_id']
        pend_qty = 0
        if vch_type == "Sale chalan" | vch_type == "Purchase Return chalan":
            voucher_type = 1
            res = minusqtyupdate(id=item_id, qty=request.json['prov_qty'])

        elif vch_type == "Purchase chalan" | vch_type == "Sale Return chalan":
            voucher_type = 2
            res = addqtyupdate(id=item_id, qty=request.json['prov_qty'])
        
    # tim1 = request.json['tim1']
    # tim2 = request.json['tim2']
    # tim3 = request.json['tim3']
    # tim4 = request.json['tim4']
    # tim5 = request.json['tim5']
    # tim6 = request.json['tim6']
    # tim7 = request.json['tim7']
    # tim8 = request.json['tim8']

    my_data = Issuedchalan_det(alter_id=alter_id, item_id=item_id, hsn=hsn, godown_id=godown_id, item_qty=item_qty, rate_per_piece=rate_per_piece,
                               taxlessvalue_per_item=taxlessvalue_per_item, user_id=user_id, hsn_desc=hsn_desc, gst_percentage=gst_percentage,
                               cgst=cgst, sgst=sgst, orderno=orderno, prov_qty=prov_qty, pend_qty=pend_qty, status=status,
                               table_state=table_state,voucher_type=voucher_type)

    db.session.add(my_data)
    db.session.commit()

    

    return issuedchalan_det_schema.jsonify(my_data)


# ============================================Edit Sales Order Det Ledgers==============================================================================


@issuedchalan_det.route("/chalanitemupdate/<id>", methods=['PUT'])
def chalanitemupdate(id):
    chalan_det = Issuedchalan_det.query.get(id)

    if chalan_det.voucher_type == 1:
        addqtyupdate(id=chalan_det.item_id, qty=chalan_det.item_qty)
        minusqtyupdate(id=request.json['item_id'], qty=request.json['item_qty'])
    elif chalan_det.voucher_type == 2:
        minusqtyupdate(id=request.json['item_id'], qty=request.json['item_qty'])
        addqtyupdate(id=chalan_det.item_id, qty=chalan_det.item_qty)

    alter_id = (db.session.query(
        Issuedchalan_det.alter_id).count()) + 1
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

    chalan_det.alter_id = alter_id
    chalan_det.item_id = item_id
    chalan_det.hsn = hsn
    chalan_det.godown_id = godown_id
    chalan_det.item_qty = item_qty
    chalan_det.rate_per_piece = rate_per_piece
    chalan_det.taxlessvalue_per_item = taxlessvalue_per_item
    chalan_det.user_id = user_id
    chalan_det.hsn_desc = hsn_desc
    chalan_det.gst_percentage = gst_percentage
    chalan_det.cgst = cgst
    chalan_det.sgst = sgst

    db.session.commit()
    return issuedchalan_det_schema.jsonify(chalan_det)


# ============================================Fetch Sales Order Det Ledgers==============================================================================
# ============================================Get Purchase order det by state =======================================================

@issuedchalan_det.route('/purchase_chalan_data', methods=['GET'])
def purchase_chalan_data():
    all_data = Issuedchalan_det.query.filter_by(table_state=1, voucher_type=2).all()
    res = issuedchalans_det_schema.dump(all_data)
    print(res)
    return jsonify(res)

# ============================================DELETE All Purchase Order Det Ledgers==============================================================================

@issuedchalan_det.route('/reloadPurchasechalan/<user_id>', methods=['DELETE'])
def reloadPurchasechalan(user_id):
    print(user_id)
    alldata = Issuedchalan_det.query.filter_by(
        table_state=1, user_id=user_id, voucher_type=2).all()

    res = issuedchalans_det_schema.dump(alldata)

    # for x in res:
    #     print(x['item_qty'])
    #     addqtyupdate(id=x['item_id'], qty=x['item_qty'])

    all_data = Issuedchalan_det.query.filter_by(
        table_state=1, user_id=user_id, voucher_type=2).delete()

    db.session.commit()
    return issuedchalan_det_schema.jsonify(res)
