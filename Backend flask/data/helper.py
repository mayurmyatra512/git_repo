from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det, Issuedchalan, Issuedchalan_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date
from sqlalchemy import select, func, update, delete


helper = Blueprint('helper', __name__)

ma = Marshmallow(app)


class IssuedChalanDetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'chalanno', 'item_id', 'hsn', 'godown_id', 'item_qty', 'rate_per_piece', 'taxlessvalue_per_item', 'tim1',
                  'tim2', 'tim3', 'tim4', 'tim5', 'tim6', 'tim7', 'tim8', 'table_state', 'user_id', 'hsn_desc', 'gst_percentage', 'cgst', 'sgst', 'orderno', 'prov_qty', 'pend_qty', 'status')


issuedchalan_det_schema = IssuedChalanDetSchema()
issuedchalans_det_schema = IssuedChalanDetSchema(many=True)


def updatechalanState(chalanno, user_id):

    all_data = Issuedchalan_det.query.filter_by(
        user_id=user_id, table_state=1).update(dict(chalanno=chalanno, table_state=0))

    db.session.commit()
    return issuedchalan_det_schema.jsonify(all_data)
