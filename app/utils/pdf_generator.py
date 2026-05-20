from flask import url_for
from fpdf import FPDF
from flask import current_app
import os


class PDF(FPDF):

    def header(self):
        self.set_font('Arial', 'B', 16)

        self.cell(0, 10, 'Reporte Clientes', 0, 1, 'C')


def generate_pdf(data):
    pdf = PDF()

    pdf.add_page()

    pdf.set_font('Arial', size=12)

    for row in data:
        pdf.cell(0, 10,
                 f'{row[1]} - {row[2]} - {row[3]}',
                 ln=True)

    pdf_path = os.path.join(
        current_app.root_path,
        'static',
        'export',
       'clientes.pdf'

    )

    pdf.output(pdf_path)

    return  pdf_path
    # pdf.output('clientes.pdf')
