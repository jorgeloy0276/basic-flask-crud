# app/__init__.py

from flask import Flask
from flask_mysqldb import MySQL


from config import Config

# Instancia global MySQL
mysql = MySQL()

def create_app():

    # Crear aplicación Flask
    app = Flask(__name__)

    # Cargar configuraciones
    app.config.from_object(Config)


    # Inicializar MySQL
    mysql.init_app(app)

    # Importar rutas desde [app/routes/client_routes.py
    # client_bp = Blueprint(    'client',    __name__)
    from app.routes.client_routes import client_bp

    # Registrar Blueprint
    app.register_blueprint(client_bp)

    # @app.route('/')
    # def index():
    #     return "Mensaje de hola mundo"
    #print(f' Las rutas son: {app.url_map}')
    return app