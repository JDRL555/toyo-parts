from utils.database import db

class Categories(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  
  def __init__(self, name):
    self.name = name  
    
class Brands(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  
  def __init__(self, name):
    self.name = name  
class Parts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(50))
  quantity = db.Column(db.Integer)
  description = db.Column(db.String(200))
  cost = db.Column(db.Float, nullable=True)
  price = db.Column(db.Float)
  inventory = db.Column(db.Float, nullable=True)
  brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
  
  def __init__(self, code, quantity, description, cost, price, inventory, brand_id, category_id):
    self.code = code
    self.quantity = quantity
    self.description = description
    self.cost = cost
    self.price = price
    self.inventory = inventory
    self.brand_id = brand_id
    self.category_id = category_id