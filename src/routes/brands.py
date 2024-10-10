from flask import Blueprint, request
from src.controllers import brands as brand_controller

brands_routes = Blueprint("brands_routes", __name__)

@brands_routes.get("/brands")
def get_brands():
  return brand_controller.get_brands()

@brands_routes.post("/brands")
def post_brand():
  return brand_controller.create_brand(request.form)

@brands_routes.patch("/brands/<id>")
def patch_brand(id):
  return brand_controller.update_brand(id, request.form)

@brands_routes.delete("/brands/<id>")
def delete_brand(id):
  return brand_controller.delete_brand(id)