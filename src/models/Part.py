from utils.database import db

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  
  def __init__(self, name):
    self.name = name  
    
class Brand(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  
  def __init__(self, name):
    self.name = name  
class Part(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(50), unique=True)
  quantity = db.Column(db.Integer)
  description = db.Column(db.String(200))
  cost = db.Column(db.Float, nullable=True)
  price = db.Column(db.Float)
  inventory = db.Column(db.Integer, nullable=True)
  brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
  
  def __init__(self, code, quantity, description, cost, price, brand_id, category_id):
    self.code = code
    self.quantity = quantity
    self.description = description
    self.cost = cost
    self.price = price
    self.brand_id = brand_id
    self.category_id = category_id