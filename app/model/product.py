from app import db
from datetime import datetime
from app.model.suplier import Supliers

class Products(db.Model):
    id          = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    name        = db.Column(db.String(150), nullable=False)
    stock       = db.Column(db.Integer(), nullable=False)
    price       = db.Column(db.Integer(), nullable=False)
    created_at  = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime,default=datetime.utcnow)
    suplier_id  = db.Column(db.BigInteger,db.ForeignKey(Supliers.id))
    supliers    = db.relationship("Supliers",backref="suplier_id")


def __repr__(self):
        return '<Product {}>'.format(self.name)