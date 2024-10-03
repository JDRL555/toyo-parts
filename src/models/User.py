from utils.database import db

class Role(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  
  def __init__(self, name):
    self.name = name

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(100))
  email = db.Column(db.String(100, unique=True))
  password = db.Column(db.String(500))
  role = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
  
  def __init__(self, fullname, email, password):
    self.fullname = fullname
    self.email = email
    self.password = password