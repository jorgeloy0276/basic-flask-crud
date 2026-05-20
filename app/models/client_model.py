from app import mysql


class Client:
    def __init__(self, id=None, name=None, email=None, phone=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

        # =========================
        # OBTENER TODOS
        # =========================

    @staticmethod
    def get_all(search='', page=1, per_page=10):
        cursor = mysql.connection.cursor()

        # Realiza el calculo para mostrar la cantidad de regitroa por pagin
        # Ej:   (page = 1 - 1) * 3
        #        (0 * 3)
        #  offset = 0 [Muestra los primeros 3 registros]
        #  offset = 1 [Muestra los del 4 al 6 ] y asi sucesivamente
        offset = (page - 1) * per_page

        query = """
                SELECT *
                FROM clients
                WHERE name LIKE %s
                   OR email LIKE %s
                   OR phone LIKE %s LIMIT %s
                OFFSET %s;
                """

        cursor.execute(
            query,
            (f'%{search}%', f'%{search}%', f'%{search}%', per_page, offset)
        )

        data = cursor.fetchall()

        return data

    # =========================
    # CONTAR REGISTROS
    # =========================

    @staticmethod
    def count(search=''):
        cursor = mysql.connection.cursor()
        # Cuenta la cantidad de registos leidos de la tabla
        query = """
                SELECT COUNT(*) \
                FROM clients
                WHERE name LIKE %s
                   OR email LIKE %s
                   OR phone LIKE %s \
                """

        cursor.execute(query, (f'%{search}%', f'%{search}%', f'%{search}%'))

        total = cursor.fetchone()[0]

        return total

    # =========================
    # INSERTAR
    # =========================

    def save(self):
        cursor = mysql.connection.cursor()

        query = """
                INSERT INTO clients(name, email, phone)
                VALUES (%s, %s, %s) \
                """

        cursor.execute(
            query,
            (self.name, self.email, self.phone)
        )

        mysql.connection.commit()

    # =========================
    # OBTENER POR ID
    # =========================

    @staticmethod
    def get_by_id(id):
        cursor = mysql.connection.cursor()

        query = "SELECT * FROM clients WHERE id = %s"

        cursor.execute(query, (id,))

        return cursor.fetchone()

    # =========================
    # ACTUALIZAR
    # =========================
    def update(self):
        cursor = mysql.connection.cursor()

        query = """
                UPDATE clients
                SET name=%s,
                    email=%s,
                    phone=%s
                WHERE id = %s \
                """

        cursor.execute(
            query,
            (self.name, self.email, self.phone, self.id)
        )

        mysql.connection.commit()
  # =========================
    # ELIMINAR
    # =========================
    @staticmethod
    def delete(id):

        cursor = mysql.connection.cursor()

        query = "DELETE FROM clients WHERE id = %s"

        cursor.execute(query, (id,))

        mysql.connection.commit()