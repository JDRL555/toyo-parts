from flask import Blueprint

users_routes = Blueprint("users", __name__)

@users_routes.get("/")
def get_users():
  return 'Get users'

@users_routes.post("/")
def post_users():
  return 'Post users'

@users_routes.patch("/")
def patch_users():
  return 'Patch users'

@users_routes.delete("/")
def delete_users():
  return 'Delete users'