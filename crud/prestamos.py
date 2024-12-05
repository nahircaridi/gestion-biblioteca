from crud.db_connection import create_connection

def add_prestamo(libro_id, fecha_prestamo, fecha_devolucion, usuario):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Prestamos (libro_id, fecha_prestamo, fecha_devolucion, usuario) VALUES (?, ?, ?, ?)",
                       (libro_id, fecha_prestamo, fecha_devolucion, usuario))
        conn.commit()

def get_prestamos():
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Prestamos")
        return cursor.fetchall()

def update_prestamo(prestamo_id, libro_id, fecha_prestamo, fecha_devolucion, usuario):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Prestamos SET libro_id = ?, fecha_prestamo = ?, fecha_devolucion = ?, usuario = ? WHERE id = ?",
                       (libro_id, fecha_prestamo, fecha_devolucion, usuario, prestamo_id))
        conn.commit()

def delete_prestamo(prestamo_id):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Prestamos WHERE id = ?", (prestamo_id,))
        conn.commit()
