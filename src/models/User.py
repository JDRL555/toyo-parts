from flask_login import UserMixin
from utils.database import db

class Roles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  
  def __init__(self, name):
    self.name = name

class Users(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(500))
  role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
  
  def __init__(self, fullname, email, password, role_id):
    self.fullname = fullname
    self.email = email
    self.password = password
    self.role_id = role_id