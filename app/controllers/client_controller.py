from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from app.utils.pdf_generator import generate_pdf
from flask import send_file

from app.models.client_model import Client


class ClientController:
    # =========================
    # LISTAR
    # =========================
    @staticmethod
    def index():
        search = request.args.get('search', '')
        page = int(request.args.get('page', 1))

        per_page = 5

        clients = Client.get_all(search, page, per_page)

        total = Client.count(search)

        total_pages = (total + per_page - 1) // per_page

        total = Client.count()
        return render_template(
            'clients/index.html',
            clients=clients,
            search=search,
            page=page,
            total_pages=total_pages
        )

        # =========================
        # AGREGAR
        # =========================

    @staticmethod
    def add():
        if request.method == 'POST':
            client = Client(
                name=request.form['name'],
                email=request.form['email'],
                phone=request.form['phone']
            )

            client.save()

            return redirect(url_for('client.index'))

        return render_template('clients/add.html')

        # =========================
        # EDITAR
        # =========================

    @staticmethod
    def edit(id):

        data = Client.get_by_id(id)

        if request.method == 'POST':
            client = Client(
                id=id,
                name=request.form['name'],
                email=request.form['email'],
                phone=request.form['phone']
            )

            client.update()

            return redirect(url_for('client.index'))

        return render_template(
            'clients/edit.html',
            client=data
        )

    # =========================
    # ELIMINAR
    # =========================
    @staticmethod
    def delete(id):

        Client.delete(id)

        return redirect(url_for('client.index'))

    # =========================
    # EXPORTAR A PDF
    # =========================

    @staticmethod
    def export_pdf():

        data = Client.get_all()

        pdf_path= generate_pdf(data)

        #return redirect(url_for('client.index'))
        return send_file(pdf_path, as_attachment=True,download_name='clientes.pdf' ,mimetype='application/pdf')



  # =========================
    # JSON API
    # =========================
    @staticmethod
    def json_data():

        data = Client.get_all()

        result = []

        for row in data:

            result.append({
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3]
            })

        return jsonify(result)