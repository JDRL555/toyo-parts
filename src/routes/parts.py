from flask import Blueprint

parts_routes = Blueprint("parts", __name__)

@parts_routes.get("/")
def get_parts():
  return 'Get parts'

@parts_routes.post("/")
def post_parts():
  return 'Post parts'

@parts_routes.patch("/")
def patch_parts():
  return 'Patch parts'

@parts_routes.delete("/")
def delete_parts():
  return 'Delete parts'