from flask import Flask

from src.routes import parts, auth, users 

app = Flask(__name__)

app.register_blueprint(parts)
app.register_blueprint(auth)
app.register_blueprint(users)

if __name__ == "main":
  app.run(debug=True)