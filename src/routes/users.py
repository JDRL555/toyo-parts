from flask import Blueprint, request, redirect, flash
from src.controllers import users as user_controller

users_routes = Blueprint("users", __name__)

@users_routes.get("/users")
def get_users():
  return user_controller.get_users()

@users_routes.post("/users")
def post_user():
  error = user_controller.create_user(request.form)
  if error[1] != 201:
    flash(error[0]["message"])
    return redirect("/register")
  return redirect("/")

@users_routes.patch("/users/<id>")
def patch_users(id):
  return user_controller.update_user(id, request.form)

@users_routes.delete("/users/<id>")
def delete_users(id):
  return user_controller.delete_user(id)