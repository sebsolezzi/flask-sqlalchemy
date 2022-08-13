from app import app
from utils.db import db

#cuando arranque la aplicacion va llamarse esta funcion
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)