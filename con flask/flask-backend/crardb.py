from app import app
from extensions import db
from models import User

with app.app_context():
    users = User.query.all()
    if users:
        print("Usuarios registrados:")
        for user in users:
            print(f"ID: {user.id}, Email: {user.email}")
    else:
        print("No hay usuarios registrados.")