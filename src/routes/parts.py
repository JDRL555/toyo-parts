from flask import Blueprint, request, redirect
from src.controllers import parts as part_controller

parts_routes = Blueprint("parts", __name__)

@parts_routes.get("/parts")
def get_parts():
  return part_controller.get_parts()

@parts_routes.post("/parts")
def post_parts():
  respuesta = part_controller.create_part(request.form)
  
  if respuesta[1] != 201:
    return respuesta
  
  return redirect("/")

@parts_routes.patch("/parts/<id>")
def patch_parts(id):
  return 'Patch parts'

@parts_routes.delete("/parts/<id>")
def delete_parts(id):
  return 'Delete parts'