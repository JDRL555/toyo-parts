from flask import Blueprint

auth_routes = Blueprint("auth", __name__)

@auth_routes.post("/login")
def login():
  return 'Login user'

@auth_routes.post("/logout")
def logout():
  return 'Logout user'