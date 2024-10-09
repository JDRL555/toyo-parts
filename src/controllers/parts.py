from src.models.Part import Parts, Categories, Brands
from utils.database import db

def get_parts_len():
  return len(Parts.query.all())

def get_parts(page = 1):
  global parts
  list_parts = []
  
  try:
    parts = Parts.query.paginate(page=page, per_page=29)
  except:
    return []
  
  if len(parts.items) == 0:
    return []
  
  for part in parts.items:
    brand = Brands.query.get(part.brand_id)
    category = Categories.query.get(part.category_id)

    list_parts.append({
      "id": part.id,
      "code": part.code,
      "quantity": part.quantity,
      "description": part.description,
      "cost": part.cost,
      "price": part.price,
      "inventory": part.inventory,
      "brand": {
        "id": brand.id,
        "name": brand.name,
      },
      "category": {
        "id": category.id,
        "name": category.name,
      },
    })
    
  return list_parts

def create_part(data):
  expected_fields = ["code", "description", "quantity", "brand_id", "category_id", "cost", "price", "inventory"]
  
  for key in data.keys():
    if key not in expected_fields:
      return {
        "message": "Informacion invalida"
      }, 400
      
  brand = Brands.query.get(data.get("brand_id"))
  category = Categories.query.get(data.get("category_id"))
  
  if not brand:
    return {
        "message": "Marca no encontrada"
      }, 404
    
  if not category:
    return {
        "message": "Categoria no encontrada"
      }, 404
  
  part = {
    "code": data.get("code"),
    "description": data.get("description"),
    "quantity": data.get("quantity"),
    "brand_id": data.get("brand_id"),
    "category_id": data.get("category_id"),
    "cost": data.get("cost"),
    "price": data.get("price"),
    "inventory": data.get("inventory"),
  }
  
  new_part = Parts(**part)
  
  db.session.add(new_part)
  db.session.commit()
  
  return {
    "message": "Parte creada exitosamente!"
  }, 201