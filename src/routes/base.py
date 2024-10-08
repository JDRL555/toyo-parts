from flask import Blueprint, render_template, request
from flask_login import current_user
from src.controllers import parts as part_controller
from src.models.User import Roles

base_routes = Blueprint("base_routes", __name__)

@base_routes.get("/")
def index_page():
  if current_user.is_authenticated:
    global page
    
    try:
      page = int(request.args.get("page")) or 1
    except:
      page = 1
      
    parts = part_controller.get_parts(page=page)
    
    role = Roles.query.get(current_user.role_id)
    
    if role.name != "cliente":
      return render_template("pages/admin.html", data={ 
      "parts": parts,
      "parts_len": part_controller.get_parts_len()  
    })
    
    return render_template("pages/parts.html", data={ 
      "parts": parts,
      "parts_len": part_controller.get_parts_len()  
    })
  return render_template("pages/index.html")

@base_routes.get("/register")
def register_page():
  return render_template("pages/register.html")