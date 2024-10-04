from utils.database import db
from src.routes import parts, brands, categories, auth, users, roles, base
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

template_dir = os.path.abspath('src/public/templates')

app = Flask(__name__, template_folder=template_dir)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app=app)

with app.app_context():
  db.create_all()

app.register_blueprint(base.base_routes)
app.register_blueprint(parts.parts_routes)
app.register_blueprint(brands.brands_routes)
app.register_blueprint(categories.categories_routes)
app.register_blueprint(auth.auth_routes)
app.register_blueprint(users.users_routes)
app.register_blueprint(roles.roles_routes)

if __name__ == "__main__":
  app.run(debug=True)