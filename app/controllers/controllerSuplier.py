from app.model.suplier import Supliers
from app import response,db
from flask import request,jsonify
from app import db

def store():
    try:
        nama_suplier = request.json['nama_suplier']
        email = request.json['email']
        phone_number = request.json['phone_number']
        suplier = Supliers(nama_suplier=nama_suplier, email=email, phone_number=phone_number)
        db.session.add(suplier)
        db.session.commit()
        return response.ok('', 'Successfully create Suplier !')
    except Exception as e:
        print(e)

def index():
    try:
        id = request.args.get('id')
        suplier = Supliers.query.filter_by(id = id).all()
        data = transform(suplier)
        return response.ok(data,"Data Suplier Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        nama_suplier = request.json['nama_suplier']
        email = request.json['email']
        phone_number = request.json['phone_number']

        suplier = Supliers.query.filter_by(id = id).first()
        suplier.nama_suplier = nama_suplier
        suplier.email = email
        suplier.phone_number = phone_number
        db.session.commit()
        return response.ok('', 'Successfully update Suplier !')
    except Exception as e:
        print(e)

def show(id):
    try:
        suplier = Supliers.query.filter_by(id=id).first()
        if not suplier:
            return response.badRequest([], 'Empty....')
        data = singleTransform(suplier, withProduct=False)
        return response.ok(data,"Data Suplier Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        suplier = Supliers.query.filter_by(id = id).first()
        if not suplier:
            return response.badRequest([], 'Empty....')
        db.session.delete(suplier)
        db.session.commit()
        return response.ok('', 'Successfully delete Suplier !')
    except Exception as e:
        print(e)


def transform(suplier):
    array = []
    for i in suplier:
        array.append(singleTransform(i))
    return array


def singleTransform(suplier, withProduct=True):
    data = {
        'id' : suplier.id,
        'nama_suplier': suplier.nama_suplier,
        'email': suplier.email,
        'phone_number': suplier.phone_number,
        'created_at': suplier.created_at,
        'updated_at': suplier.updated_at
    }

    if withProduct:
        products = []
        for i in supliers.products:
            products.append({
                'id':i.id,
                'name': i.name,
                'stok': i.stok,
                'price': i.price,
            })
            data['products'] = products

    return data