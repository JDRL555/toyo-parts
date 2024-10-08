from flask import jsonify
from src.models.Part import Parts, Categories, Brands

def get_parts_len():
  return len(Parts.query.all())

def get_parts(page = 1):
  global parts
  list_parts = []
  
  try:
    parts = Parts.query.order_by("description").paginate(page=page, per_page=29)
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