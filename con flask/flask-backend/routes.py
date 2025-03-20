from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from models import Task, db
from auth import login, register
from models import User  # Asegúrate de importar el modelo User
api_blueprint = Blueprint('api', __name__)

# Rutas de autenticación
@api_blueprint.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=str(user.id))
        print(f"Generated Token: {access_token}")  # Imprime el token en los logs
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

@api_blueprint.route('/api/auth/register', methods=['POST'])
def register_route():
    return register()

# Rutas de tareas
@api_blueprint.route('/api/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify({'tasks': [{'id': t.id, 'title': t.title, 'description': t.description} for t in tasks]}), 200

@api_blueprint.route('/api/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    task = Task(title=data['title'], description=data['description'], user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully', 'task': {'id': task.id, 'title': task.title}}), 201