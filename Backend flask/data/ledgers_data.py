from flask import Blueprint, jsonify, request
from .models import Ledger_master, Item_master, Ledger_groups
from flask_marshmallow import Marshmallow
from . import db
from . import app
from datetime import date


ledgers_data = Blueprint('ledgers_data', __name__)

ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alt_id', 'alt_date', 'ledger_name', 'ledger_alias', 'cgroup_id', 'ledger_type', 'date', 'address', 'pincode', 'continent', 'subcontinent', 'country', 'subcountry', 'state', 'substate', 'district', 'subdistrict', 'city', 'subcity', 'area', 'email', 'office_mob',
                  'personal_mob', 'salesperson_name', 'accountmanager_id', 'creditlimit', 'creditdays', 'pdcdays', 'gstno', 'panno', 'ledgeropening', 'branch_id', 'created_on', 'modified_on', 'from_user', 'cm_1', 'cm_2', 'cm_3', 'cm_4', 'cm_5', 'cm_6', 'cm_7', 'cm_8', 'cm_9', 'cm_10')


ledger_schema = UserSchema()
ledgers_schema = UserSchema(many=True)

# ============================================List of Ledgers==============================================================================


@ledgers_data.route('/ledgers', methods=['GET'])
def ledgers():
    all_data = Ledger_master.query.all()
    res = ledgers_schema.dump(all_data)
    return jsonify(res)

# ============================================Get Ledgers==============================================================================


@ledgers_data.route('/ledger_det/<id>', methods=['GET'])
def ledger_det(id):
    ledger = Ledger_master.query.get(id)
    return ledger_schema.jsonify(ledger)

# ============================================Update Ledgers==============================================================================


@ledgers_data.route('/ledger_update/<id>', methods=['PUT'])
def ledger_update(id):
    ledger = Ledger_master.query.get(id)

    ledger.ledger_name = request.json['ledger_name']
    ledger.ledger_alias = request.json['ledger_alias']
    ledger.ledger_type = request.json['ledger_type']
    ledger.cgroup_id = request.json['cgroup_id']
    if request.json['date'] == "":
        ledger.date = date.today()
    else:
        ledger.date = request.json['date']
    ledger.address = request.json['address']
    ledger.pincode = request.json['pincode']
    ledger.continent = request.json['continent']
    ledger.subcontinent = request.json['subcontinent']
    ledger.country = request.json['country']
    ledger.subcountry = request.json['subcountry']
    ledger.state = request.json['state']
    ledger.substate = request.json['substate']
    ledger.district = request.json['district']
    ledger.subdistrict = request.json['subdistrict']
    ledger.city = request.json['city']
    ledger.subcity = request.json['subcity']
    ledger.area = request.json['area']
    ledger.email = request.json['email']
    ledger.office_mob = request.json['office_mob']
    ledger.personal_mob = request.json['personal_mob']
    # accountmanager_id = request.json['led_accmanager']
    ledger.creditlimit = request.json['creditlimit']
    ledger.creditdays = request.json['creditdays']
    ledger.pdcdays = request.json['pdcdays']
    ledger.gstno = request.json['gstno']
    ledger.panno = request.json['panno']
    ledger.ledgeropening = request.json['ledgeropening']

    db.session.commit()
    return ledger_schema.jsonify(ledger)


# ============================================Delete Ledgers==============================================================================

@ledgers_data.route("/ledger_delete/<id>", methods=['DELETE'])
def ledger_delete(id):
    ledger = Ledger_master.query.get(id)
    db.session.delete(ledger)
    db.session.commit()
    return ledger_schema.jsonify(ledger)


# ============================================Add New Ledgers==============================================================================

@ledgers_data.route('/newledger', methods=['POST'])
def newledger():

    ledger_name = request.json['ledger_name']
    ledger_alias = request.json['ledger_alias']
    ledger_type = request.json['ledger_type']
    cgroup_id = request.json['cgroup_id']
    if request.json['date'] == "":
        date = date.today()
    else:
        date = request.json['date']
    address = request.json['address']
    pincode = request.json['pincode']
    continent = request.json['continent']
    subcontinent = request.json['subcontinent']
    country = request.json['country']
    subcountry = request.json['subcountry']
    state = request.json['state']
    substate = request.json['substate']
    district = request.json['district']
    subdistrict = request.json['subdistrict']
    city = request.json['city']
    subcity = request.json['subcity']
    area = request.json['area']
    email = request.json['email']
    office_mob = request.json['office_mob']
    personal_mob = request.json['personal_mob']
    # accountmanager_id = request.json['accmanager']
    creditlimit = request.json['creditlimit']
    creditdays = request.json['creditdays']
    pdcdays = request.json['pdcdays']
    gstno = request.json['gstno']
    panno = request.json['panno']
    ledgeropening = request.json['ledgeropening']

    my_data = Ledger_master(ledger_name=ledger_name, ledger_alias=ledger_alias, cgroup_id=cgroup_id, ledger_type=ledger_type, date=date, address=address, pincode=pincode, continent=continent, subcontinent=subcontinent, country=country, subcountry=subcountry, state=state, substate=substate,
                            district=district, subdistrict=subdistrict, city=city, subcity=subcity, area=area, email=email, office_mob=office_mob, personal_mob=personal_mob, creditlimit=creditlimit, creditdays=creditdays, pdcdays=pdcdays, gstno=gstno, panno=panno, ledgeropening=ledgeropening)
    db.session.add(my_data)
    db.session.commit()
    return ledger_schema.jsonify(my_data)
