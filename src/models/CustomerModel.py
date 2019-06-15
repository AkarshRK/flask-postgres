# src/models/CustomerModel.py
from . import db
import datetime
from marshmallow import fields, Schema
from sqlalchemy import desc

class CustomerModel(db.Model):
  """
  Customer Model
  """

  __tablename__ = 'customers'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  dob = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.name = data.get('name')
    self.dob = data.get('dob')
    self.updated_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.updated_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_customers():
    return CustomerModel.query.all()
    
  @staticmethod
  def get_n_customers(n):
    return CustomerModel.query.order_by(desc(CustomerModel.dob)).limit(n).all()
  
  @staticmethod
  def get_one_customer(id):
    return CustomerModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class CustomerSchema(Schema):
  """
  Customer Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  dob = fields.Str(required=True)
  updated_at = fields.DateTime(dump_only=True)