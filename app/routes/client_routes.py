from flask import Blueprint

from app.controllers.client_controller import ClientController

client_bp = Blueprint('client', __name__)

# LISTAR
client_bp.route('/')(ClientController.index)

# AGREGAR
client_bp.route('/add', methods=['GET', 'POST'])(ClientController.add)


# EDITAR
client_bp.route(
    '/edit/<int:id>',
    methods=['GET', 'POST']
)(
    ClientController.edit
)

# ELIMINAR
client_bp.route('/delete/<int:id>')(
    ClientController.delete
)

# PDF
client_bp.route('/pdf')(ClientController.export_pdf)

# JSON
client_bp.route('/json')(ClientController.json_data)