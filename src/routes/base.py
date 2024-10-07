from flask import Blueprint, render_template
from flask_login import current_user

base_routes = Blueprint("base_routes", __name__)

@base_routes.get("/")
def index_page():
  if current_user.is_authenticated:
    return render_template("pages/parts.html")
  return render_template("pages/index.html")

@base_routes.get("/register")
def register_page():
  return render_template("pages/register.html")