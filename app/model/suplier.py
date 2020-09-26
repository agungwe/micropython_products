from app import db
from datetime import datetime

class Supliers(db.Model):
    id          = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    nama_suplier= db.Column(db.String(140), unique=True, nullable=False)
    email       = db.Column(db.String(100), unique=True, nullable=True)
    phone_number= db.Column(db.String(20), nullable=True)
    created_at  = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime,default=datetime.utcnow)
    products    = db.relationship("Products",
                                  lazy    ='select',
                                  backref =db.backref('products',lazy ='joined'))

def __repr__(self):
        return '<Suplier {}>'.format(self.nama_suplier)