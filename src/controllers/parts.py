from flask import jsonify
from src.models.Part import Parts, Categories, Brands

def get_parts(limit = 10):
  parts = Parts.query.limit(limit).all()
  list_parts = []
  
  for part in parts:
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
    
  return jsonify(list_parts)