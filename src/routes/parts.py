from flask import Blueprint, request, redirect, flash
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

@parts_routes.post("/parts/<id>")
def edit_parts(id):
  respuesta = part_controller.edit_part(id, request.form)
  
  if respuesta[1] != 200:
    flash(respuesta[0]["message"])
    return redirect(f"/edit/{id}")
  
  return redirect('/')

@parts_routes.get("/parts/<id>")
def delete_parts(id):
  respuesta = part_controller.delete_part(id)
  
  if respuesta[1] != 200:
    flash(respuesta[0]["message"])
  
  return redirect('/')