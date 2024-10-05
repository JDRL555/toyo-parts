from src.models.Part import Categories, Brands, Parts
from data.categories import categories
from data.brands import brands
import json

json_file = open("data/parts.json", "r")
parts_list = json.load(json_file)

def seed(database):
  if len(Categories.query.all()) == 0:
    for category in categories:
      new_category = Categories(category)
      database.session.add(new_category)
      database.session.commit()
      
  if len(Brands.query.all()) == 0:
    for brand in brands:
      new_brand = Brands(brand)
      database.session.add(new_brand)
      database.session.commit()
    
  if len(Parts.query.all()) == 0:
    for part in parts_list:
      brand = Brands.query.filter_by(name=part["brand"]).first()
      category = Categories.query.filter_by(name=part["category"]).first()
      
      part_dict = {
        "code": part["code"],
        "quantity": part["quantity"],
        "description": part["description"],
        "cost": part["cost"],
        "price": part["price"],
        "inventory": part["inventory"],
        "brand_id": brand.id,
        "category_id": category.id,
      }
      
      new_part = Parts(**part_dict)
      database.session.add(new_part)
      database.session.commit()