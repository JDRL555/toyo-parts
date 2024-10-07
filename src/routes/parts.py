from flask import Blueprint
from src.controllers import parts as part_controller

parts_routes = Blueprint("parts", __name__)

@parts_routes.get("/parts")
def get_parts():
  return part_controller.get_parts()

@parts_routes.post("/parts")
def post_parts():
  return 'Post parts'

@parts_routes.patch("/parts/<id>")
def patch_parts(id):
  return 'Patch parts'

@parts_routes.delete("/parts/<id>")
def delete_parts(id):
  return 'Delete parts'