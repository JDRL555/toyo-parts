from flask_login import login_user, logout_user
from bcrypt import checkpw
from src.models.User import Users

def login(email, password):
  user = Users.query.filter_by(email=email).first()
  
  if not user:
    return {
      "message": "Correo incorrecto o el usuario no existe"
    }, 404
    
  if not checkpw(password=password.encode("utf-8"), hashed_password=user.password.encode("utf-8")):
    return {
      "message": "Clave incorrecta"
    }, 401
    
  login_user(user)
    
  return {
      "message": "Sesion iniciada correctamente!"
    }, 200
  
def logout():
  logout_user()