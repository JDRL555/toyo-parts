from flask import jsonify

from src.models.Part import Categories
from utils.database import db

def get_categories():
  categories = Categories.query.all()
  list_categories = [
    { 
      "id": categorie.id, 
      "name": categorie.name 
    } for categorie in categories
  ]
  return jsonify(list_categories)

def create_category(data):
  if not data.get("name"):
    return {
      "message": "Informacion invalida. Se espera un name"
    }, 400
  
  new_categorie = Categories(data.get("name"))
  
  try:
    db.session.add(new_categorie)
    db.session.commit()    
    return {
      "message": "Categoria creada exitosamente!"
    }, 201
  except:
    return {
      "message": "La categoria ya existe"
    }, 400
    
def update_category(category_id, new_data):
  categorie = {}
  
  categorie = Categories.query.get(category_id)
  
  if not categorie:
    return {
      "message": "Categoria no encontrada"
    }, 404
  
  if new_data.get("name"): categorie.name = new_data.get("name")  

  db.session.commit()
  
  return {
    "message": "Categoria actualizada"
  }
  
def delete_category(category_id):
  categorie = Categories.query.get(category_id)
  
  if not categorie:
    return {
      "message": "Categoria no encontrada"
    }, 404
  
  db.session.delete(categorie)
  db.session.commit()
  
  return {}, 204