from flask import Blueprint, request, redirect, flash
from src.controllers import auth as auth_controller

auth_routes = Blueprint("auth", __name__)

@auth_routes.post("/login")
def login():
  error = auth_controller.login(email=request.form["email"], password=request.form["password"])
  if error[1] != 200:
    flash(error[0]["message"])
  return redirect("/")

@auth_routes.post("/logout")
def logout():
  return 'Logout user'