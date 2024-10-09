from flask import Blueprint, render_template, request, redirect
from flask_login import current_user
from src.controllers import parts as part_controller
from src.models.User import Roles
from src.models.Part import Parts, Brands, Categories

base_routes = Blueprint("base_routes", __name__)

@base_routes.get("/")
def index_page():
  if current_user.is_authenticated:
    global page
    
    try:
      page = int(request.args.get("page")) or 1
    except:
      page = 1
    
    len_last_parts = 29
    parts = part_controller.get_parts(page=page)
    parts_len = part_controller.get_parts_len()
    role = Roles.query.get(current_user.role_id)
    
    if page != 1:
      len_last_parts = len(part_controller.get_parts(page=page - 1))
    
    if role.name != "cliente":
      division = parts_len / 29
      last_page = int(division) + 1 if type(division) == float else int(division)
      total = 29 if page == 1 else ((page - 1) * len_last_parts) + len(parts)
      
      return render_template("pages/admin.html", data={ 
      "parts": parts,
      "parts_len": parts_len,
      "last_page": last_page,
      "total": total
    })
    
    return render_template("pages/parts.html", data={ 
      "parts": parts,
      "parts_len": parts_len,
      "last_page": last_page,
      "total": total  
    })
  return render_template("pages/index.html")

@base_routes.get("/register")
def register_page():
  return render_template("pages/register.html")

@base_routes.get("/create")
def create_part():
  brands = Brands.query.order_by("name").all()
  categories = Categories.query.order_by("name").all()
  role = Roles.query.get(current_user.role_id)
  if role.name != "administrador":
    return redirect("/")
  return render_template("pages/create_part.html", data={
    "brands": brands,
    "categories": categories,
  })
  
@base_routes.get("/edit/<id>")
def edit_part(id):
  part = Parts.query.get(id)
  
  if not part:
    return {
      "message": "Parte no encontrada"
    }, 404
  
  brands = Brands.query.order_by("name").all()
  categories = Categories.query.order_by("name").all()
  
  role = Roles.query.get(current_user.role_id)
  if role.name != "administrador":
    return redirect("/")
  
  return render_template("pages/edit_part.html", data={
    "code": part.code,
    "description": part.description,
    "quantity": part.quantity,
    "brand_id": part.brand_id,
    "category_id": part.category_id,
    "cost": part.cost,
    "price": part.price,
    "inventory": part.inventory,
    "brands": brands,
    "categories": categories,
  })