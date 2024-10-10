from flask import Blueprint, request
from src.controllers import categories as category_controller

categories_routes = Blueprint("categories_routes", __name__)

@categories_routes.get("/categories")
def get_categories():
  return category_controller.get_categories()

@categories_routes.post("/categories")
def post_category():
  return category_controller.create_category(request.form)

@categories_routes.patch("/categories/<id>")
def patch_category(id):
  return category_controller.update_category(id, request.form)

@categories_routes.delete("/categories/<id>")
def delete_category(id):
  return category_controller.delete_category(id)