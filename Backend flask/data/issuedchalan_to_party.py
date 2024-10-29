from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups, Sales_invoice, Sales_invoice_det, Issuedchalan, Transporter, Sales_order, Sales_order_det
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import datetime
from sqlalchemy import select, func, update
from .helper import updatechalanState
from .sales_order import sales_order_data_for_chalan
import json


issuedchalan_to_party = Blueprint('issuedchalan_to_party', __name__)

ma = Marshmallow(app)
ma2 = Marshmallow(app)


class IssuedChalanSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alter_id', 'vch_type', 'chalanno', 'chalandate', 'orderno', 'ledger_id', 'salesperson_name', 'narration', 'tot_taxlessvalue', 'CGST', 'SGST',
                  'taxpaidvalue', 'created_on', 'modified_on', 'user_id', 'transporter_id', 't_1', 't_2', 't_3', 't_4', 't_5', 't_6', 't_7', 't_8', 't_9', 't_10', 'gr_rr_no', 'veh_number', 'station', 'godows_id')

# class Transporter(ma2.Schema):
#     class Meta:
#         fields =


issuedchalan_schema = IssuedChalanSchema()
issuedchalans_schema = IssuedChalanSchema(many=True)


def postorderchalan(orderno, chalanno, user_id, godown_id):
    SO_data = sales_order_data_for_chalan(orderno)
    # print(type(res))

    # SO_data = res.json()

    alter_id = (db.session.query(Issuedchalan.alter_id).count()) + 1
    vch_type = "Sales Chalan"
    chalanno = chalanno
    ddate = datetime.today().strftime("%d/%m/%Y")
    chalandate = datetime.strptime(ddate, '%d/%m/%Y')
    print(chalandate)
    orderno = orderno

    ledger_id = SO_data.json[0]['ledger_id']
    # salesperson_name = request.json['salesperson_name']
    # narration = request.json['narration']
    # item_det_id = request.json['item_det_id']
    tot_taxlessvalue = SO_data.json[0]['tot_taxlessvalue']
    CGST = SO_data.json[0]['CGST']
    SGST = SO_data.json[0]['SGST']
    # IGST = request.json['IGST']
    taxpaidvalue = SO_data.json[0]['taxpaidvalue']
    # created_on = request.json['created_on']
    # modified_on = request.json['modified_on']
    user_id = user_id
    # transporter_id = transporter_id
    # gr_rr_no = gr_rr_no
    # veh_number = veh_number
    # station = station
    godown_id = godown_id

    my_data = Issuedchalan(alter_id=alter_id, vch_type=vch_type, chalanno=chalanno, chalandate=chalandate, orderno=orderno, ledger_id=ledger_id, tot_taxlessvalue=tot_taxlessvalue, CGST=CGST, SGST=SGST,
                           taxpaidvalue=taxpaidvalue)
    db.session.add(my_data)
    db.session.commit()

    updatechalanState(chalanno=request.json['chalanno'], user_id=user_id)

    return issuedchalan_schema.jsonify(my_data)


@issuedchalan_to_party.route('/chalan', methods=['POST'])
def chalan():

    alter_id = (db.session.query(Issuedchalan.alter_id).count()) + 1
    vch_type = request.json['vch_type']
    chalanno = request.json['chalanno']
    chalandate = request.json['chalandate']
    orderno = request.json['orderno']
    ledger_id = request.json['ledger_id']
    salesperson_name = request.json['salesperson_name']
    narration = request.json['narration']
    # item_det_id = request.json['item_det_id']
    tot_taxlessvalue = request.json['tot_taxlessvalue']
    CGST = request.json['CGST']
    SGST = request.json['SGST']
    # IGST = request.json['IGST']
    taxpaidvalue = request.json['taxpaidvalue']
    # created_on = request.json['created_on']
    # modified_on = request.json['modified_on']
    user_id = request.json['user_id']
    transporter_id = request.json['transporter_id']
    gr_rr_no = request.json['gr_rr_no']
    veh_number = request.json['veh_number']
    station = request.json['station']
    godown_id = request.json['godown_id']
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

    my_data = Issuedchalan(alter_id=alter_id, vch_type=vch_type, chalanno=chalanno, chalandate=chalandate, orderno=orderno, ledger_id=ledger_id, salesperson_name=salesperson_name, narration=narration, tot_taxlessvalue=tot_taxlessvalue, CGST=CGST, SGST=SGST,
                           taxpaidvalue=taxpaidvalue, transporter_id=transporter_id, user_id=user_id, gr_rr_no=gr_rr_no, veh_number=veh_number, station=station, godown_id=godown_id)

    db.session.add(my_data)
    db.session.commit()

    updatechalanState(chalanno=request.json['chalanno'], user_id=user_id)

    return issuedchalan_schema.jsonify(my_data)


@issuedchalan_to_party.route('/chalanno', methods=['GET'])
def chalanno():
    res = db.session.query(func.max(Issuedchalan.chalanno)).scalar()

    return jsonify(res)
