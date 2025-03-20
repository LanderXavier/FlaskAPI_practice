from flask import Flask, send_from_directory
from config import Config
from routes import api_blueprint
from extensions import db, jwt  # Import from extensions
from flask_cors import CORS  # Import CORS
from flask_jwt_extended import JWTManager

# Configuración de la aplicación
app = Flask(__name__, static_folder='../frontend', static_url_path='/frontend')
app.config.from_object(Config)
CORS(app)  # Habilita CORS para todas las rutas
# Configuración para evitar truncar cadenas largas en JSON
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json"

jwt = JWTManager(app)
# Inicializar extensiones
db.init_app(app)
jwt.init_app(app)

# Registrar rutas del backend
app.register_blueprint(api_blueprint)

# Ruta para servir el archivo principal del frontend
@app.route('/')
def index():
    return send_from_directory('../frontend', 'register.html')

# Ruta para servir archivos estáticos del frontend
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)