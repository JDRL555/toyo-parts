from flask import Blueprint

users_routes = Blueprint("users", __name__)

@users_routes.get("/users")
def get_users():
  return 'Get users'

@users_routes.post("/users")
def post_users():
  return 'Post users'

@users_routes.patch("/users/<id>")
def patch_users(id):
  return 'Patch users'

@users_routes.delete("/users/<id>")
def delete_users(id):
  return 'Delete users'