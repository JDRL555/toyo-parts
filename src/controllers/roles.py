from flask import jsonify

from src.models.User import Roles
from utils.database import db

def get_roles():
  roles = Roles.query.all()
  list_roles = [
    { 
      "id": role.id, 
      "name": role.name 
    } for role in roles
  ]
  return jsonify(list_roles)

def create_role(data):
  if not data.get("name"):
    return {
      "message": "Informacion invalida. Se espera un name"
    }, 400
  
  new_role = Roles(data.get("name"))
  
  try:
    db.session.add(new_role)
    db.session.commit()    
    return {
      "message": "Rol creado exitosamente!"
    }, 201
  except:
    return {
      "message": "El rol ya existe"
    }, 400
    
def update_role(role_id, new_data):
  role = {}
  
  role = Roles.query.get(role_id)
  
  if not role:
    return {
      "message": "Role no encontrado"
    }, 404
  
  if new_data.get("name"): role.name = new_data.get("name")  

  db.session.commit()
  
  return {
    "message": "Role actualizado"
  }
  
def delete_role(role_id):
  role = Roles.query.get(role_id)
  
  if not role:
    return {
      "message": "Role no encontrado"
    }, 404
  
  db.session.delete(role)
  db.session.commit()
  
  return {}, 204