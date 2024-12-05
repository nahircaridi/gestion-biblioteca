from crud.db_connection import create_connection

def add_autor(nombre, apellido, nacionalidad, fecha_nacimiento, genero):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Autores (nombre, apellido, nacionalidad, fecha_nacimiento, genero) VALUES (?, ?, ?, ?, ?)",
                       (nombre, apellido, nacionalidad, fecha_nacimiento, genero))
        conn.commit()

def get_autores():
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Autores")
        return cursor.fetchall()

def update_autor(autor_id, nombre, apellido, nacionalidad, fecha_nacimiento, genero):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Autores SET nombre = ?, apellido = ?, nacionalidad = ?, fecha_nacimiento = ?, genero = ? WHERE id = ?",
                       (nombre, apellido, nacionalidad, fecha_nacimiento, genero, autor_id))
        conn.commit()

def delete_autor(autor_id):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Autores WHERE id = ?", (autor_id,))
        conn.commit()
