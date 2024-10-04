from flask import Blueprint, request
from src.controllers import roles as role_controller

roles_routes = Blueprint("roles_routes", __name__)

@roles_routes.get("/roles")
def get_roles():
  return role_controller.get_roles()

@roles_routes.post("/roles")
def post_role():
  return role_controller.create_role(request.form)

@roles_routes.patch("/roles/<id>")
def patch_role(id):
  return role_controller.update_role(id, request.form)

@roles_routes.delete("/roles/<id>")
def delete_role(id):
  return role_controller.delete_role(id)