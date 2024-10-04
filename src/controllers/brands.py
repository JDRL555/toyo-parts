from flask import jsonify

from src.models.Part import Brands
from utils.database import db

def get_brands():
  brands = Brands.query.all()
  list_brands = [
    { 
      "id": brand.id, 
      "name": brand.name 
    } for brand in brands
  ]
  return jsonify(list_brands)

def create_brand(data):
  if not data.get("name"):
    return {
      "message": "Informacion invalida. Se espera un name"
    }, 400
  
  new_brand = Brands(data.get("name"))
  
  try:
    db.session.add(new_brand)
    db.session.commit()    
    return {
      "message": "Marca creada exitosamente!"
    }, 201
  except:
    return {
      "message": "La marca ya existe"
    }, 400
    
def update_brand(brand_id, new_data):
  brand = {}
  
  brand = Brands.query.get(brand_id)
  
  if not brand:
    return {
      "message": "Marca no encontrada"
    }, 404
  
  if new_data.get("name"): brand.name = new_data.get("name")  

  db.session.commit()
  
  return {
    "message": "Marca actualizada"
  }
  
def delete_brand(brand_id):
  brand = Brands.query.get(brand_id)
  
  if not brand:
    return {
      "message": "Marca no encontrada"
    }, 404
  
  db.session.delete(brand)
  db.session.commit()
  
  return {}, 204