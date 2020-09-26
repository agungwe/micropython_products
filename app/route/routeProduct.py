from app import app
from app.controllers import controllerProduct
from flask import request


@app.route('/product', methods=['POST','GET'])
def product():
    if request.method == 'POST':
        return controllerProduct.store()
    elif request.method == 'GET':
        return controllerProduct.index()


@app.route('/product/<id>', methods=['PUT','GET','DELETE'])
def productDetail(id):
    if request.method == 'GET':
        return controllerProduct.show(id)
    elif request.method == 'PUT':
        return controllerProduct.update(id)
    elif request.method == 'DELETE':
        return controllerProduct.delete(id)