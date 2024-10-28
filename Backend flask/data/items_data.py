from flask import Blueprint, jsonify, request
from .models import Item_master, Item_groups
from flask_marshmallow import Marshmallow
from . import db
from . import app
from sqlalchemy import update

items_data = Blueprint('items_data', __name__)

ma = Marshmallow(app)


class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alt_id', 'alt_date', 'item_name', 'item_alias', 'igroup_id', 'date', 'part_no', 'unit', 'alt_unit', 'brand', 'subbrand', 'category', 'subcategory', 'sbu', 'subsbu',
                  'opening_qty', 'openingvalue', 'openingmrp', 'branch_id', 'created_on', 'modified_on', 'from_user', 'im_1', 'im_2', 'im_3', 'im_4', 'im_5', 'im_6', 'im_7', 'im_8', 'im_9', 'im_10', 'hsncode', 'hsn_desc', 'gst_percentage', 'cgst', 'sgst', 'available_qty')


item_schema = ItemSchema()
itemschema = ItemSchema(many=True)

# ============================================List of Items==============================================================================


@items_data.route('/items', methods=['GET'])
def items():
    all_data = Item_master.query.all()
    res = itemschema.dump(all_data)
    return jsonify(res)


# ============================================Get Items==============================================================================


@items_data.route('/item_det/<id>', methods=['GET'])
def item_det(id):
    item = Item_master.query.get(id)
    return item_schema.jsonify(item)


# ============================================Update Items==============================================================================


@items_data.route('/item_update/<id>', methods=['PUT'])
def item_update(id):
    item = Item_master.query.get(id)

    item_name = request.json['item_name']
    item_alias = request.json['item_alias']
    igroup_id = request.json['igroup_id']
    date = request.json['date']
    part_no = request.json['part_no']
    unit = request.json['unit']
    alt_unit = request.json['alt_unit']
    brand = request.json['brand']
    subbrand = request.json['subbrand']
    category = request.json['category']
    subcategory = request.json['subcategory']
    sbu = request.json['sbu']
    subsbu = request.json['subsbu']
    opening_qty = request.json['opening_qty']
    openingmrp = request.json['openingmrp']
    openingvalue = request.json['openingvalue']
    hsncode = request.json['hsncode']
    hsn_desc = request.json['hsn_desc']
    gst_percentage = request.json['gst_percentage']
    sgst = float(gst_percentage) / 2
    cgst = float(gst_percentage) / 2

    item.item_name = item_name
    item.item_alias = item_alias
    item.igroup_id = igroup_id
    item.date = date
    item.part_no = part_no
    item.unit = unit
    item.alt_unit = alt_unit
    item.brand = brand
    item.subbrand = subbrand
    item.category = category
    item.subcategory = subcategory
    item.sbu = sbu
    item.subsbu = subsbu
    item.opening_qty = opening_qty
    item.openingmrp = openingmrp
    item.openingvalue = openingvalue
    item.hsncode = hsncode
    item.hsn_desc = hsn_desc
    item.gst_percentage = gst_percentage
    item.sgst = sgst
    item.cgst = cgst
    item.available_qty = opening_qty

    db.session.commit()
    return item_schema.jsonify(item)


# ============================================Delete Item==============================================================================

@items_data.route("/item_delete/<id>", methods=['DELETE'])
def item_delete(id):
    item = Item_master.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return item_schema.jsonify(item)


# ============================================Add New Item==============================================================================

@items_data.route('/newitem', methods=['POST'])
def newitem():

    item_name = request.json['item_name']
    item_alias = request.json['item_alias']
    igroup_id = request.json['igroup_id']
    date = request.json['date']
    part_no = request.json['part_no']
    unit = request.json['unit']
    alt_unit = request.json['alt_unit']
    brand = request.json['brand']
    subbrand = request.json['subbrand']
    category = request.json['category']
    subcategory = request.json['subcategory']
    sbu = request.json['sbu']
    subsbu = request.json['subsbu']
    opening_qty = request.json['opening_qty']
    openingmrp = request.json['openingmrp']
    openingvalue = request.json['openingvalue']
    hsncode = request.json['hsncode']
    hsn_desc = request.json['hsn_desc']
    gst_percentage = request.json['gst_percentage']
    sgst = float(gst_percentage) / 2
    cgst = float(gst_percentage) / 2

    my_data = Item_master(item_name=item_name, item_alias=item_alias, igroup_id=igroup_id, date=date, part_no=part_no, unit=unit, alt_unit=alt_unit, brand=brand,
                          subbrand=subbrand, category=category, subcategory=subcategory, sbu=sbu, subsbu=subsbu, opening_qty=opening_qty, openingmrp=openingmrp,
                          openingvalue=openingvalue, hsncode=hsncode, hsn_desc=hsn_desc, gst_percentage=gst_percentage, sgst=sgst, cgst=cgst, available_qty=opening_qty)

    db.session.add(my_data)
    db.session.commit()
    return item_schema.jsonify(my_data)

# =======================================================After sale Qty update ==============================================================


def minusqtyupdate(id, qty):


    item = Item_master.query.get(id)
    print(id)
    print (qty)
    item.available_qty = int(item.available_qty) - int(qty)

    db.session.commit()
    return item_schema.jsonify(item)


def addqtyupdate(id, qty):

    item = Item_master.query.get(id)
    item.available_qty = int(item.available_qty) + int(qty)

    db.session.commit()
    return item_schema.jsonify(item)


def itemId(name):
    id = db.session.scalar(
        db.select(Item_master.id).where(Item_master.item_name == name))
    # print(id)
    return id
