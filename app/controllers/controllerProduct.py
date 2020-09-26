from app.model.product import Products
from app import response,db
from flask import request,jsonify
from app.controllers import controllerSuplier
from app import db

import datetime


def store():
    try:
        name = request.json['name']
        stock = request.json['stock']
        price = request.json['price']
        suplier_id = request.json['suplier_id']

        product = Products(name=name, stock=stock, price=price, suplier_id=suplier_id)
        db.session.add(product)
        db.session.commit()
        
        return response.ok('', 'Successfully Create Product !')
    except Exception as e:
        print(e)


def index():
    try:
        id = request.args.get('suplier_id')
        product = Products.query.filter_by(suplier_id = id).all()
        data = transform(product)
        return response.ok(data,"Data Product Ditemukan!")
    except Exception as e:
        print(e)


def update(id):
    try:
        name = request.json['name']
        stock = request.json['stock']
        price = request.json['price']
        suplier_id = request.json['suplier_id']

        product = Products.query.filter_by(id = id).first()
        product.name = name
        product.stock = stock
        product.price = price
        product.suplier_id = suplier_id
        db.session.commit()
        return response.ok('', 'Successfully update Product!')
    except Exception as e:
        print(e)

def show(id):
    try:
        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.badRequest([], 'Empty....')
        data = singleTransform(product)
        return response.ok(data,"Data Product Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        product = Products.query.filter_by(id = id).first()
        if not product:
            return response.badRequest([], 'Empty....')
        db.session.delete(product)
        db.session.commit()
        return response.ok('', 'Successfully delete Product !')
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    print(values.suplier.id)
    print(values.suplier.nama_suplier)
    print(values.suplier.phone_number)
    data = {
        'id' : values.id,
        'name': values.name,
        'stock': values.stock,
        'price': values.price,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
        "suplier_id": values.suplier_id,
        'suplier': controllerSuplier.singleTransform(values.supliers, withPruduct=False)
    }

    return data