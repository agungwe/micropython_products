from app import app
from app.controllers import controllerSuplier
from flask import request


@app.route('/suplier', methods=['POST','GET'])
def suplier():
    if request.method == 'POST':
        return controllerSuplier.store()
    elif request.method == 'GET':
        return controllerSuplier.index()


@app.route('/suplier/<id>', methods=['PUT','GET','DELETE'])
def suplierDetail(id):
    if request.method == 'GET':
        return controllerSuplier.show(id)
    elif request.method == 'PUT':
        return controllerSuplier.update(id)
    elif request.method == 'DELETE':
        return controllerSuplier.delete(id)