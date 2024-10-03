from flask import Blueprint

auth_routes = Blueprint("auth", __name__)

@auth_routes.get("/")
def get_auth():
  return 'Get auth'

@auth_routes.post("/")
def post_auth():
  return 'Post auth'

@auth_routes.patch("/")
def patch_auth():
  return 'Patch auth'

@auth_routes.delete("/")
def delete_auth():
  return 'Delete auth'