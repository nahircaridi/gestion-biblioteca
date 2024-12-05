from crud.db_connection import create_connection

def add_libro(titulo, autor_id, ano_publicacion, genero, editorial, estado):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Libros (titulo, autor_id, ano_publicacion, genero, editorial, estado) VALUES (?, ?, ?, ?, ?, ?)",
                       (titulo, autor_id, ano_publicacion, genero, editorial, estado))
        conn.commit()

def get_libros():
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Libros")
        return cursor.fetchall()

def update_libro(libro_id, titulo, autor_id, ano_publicacion, genero, editorial, estado):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Libros SET titulo = ?, autor_id = ?, ano_publicacion = ?, genero = ?, editorial = ?, estado = ? WHERE id = ?",
                       (titulo, autor_id, ano_publicacion, genero, editorial, estado, libro_id))
        conn.commit()

def delete_libro(libro_id):
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Libros WHERE id = ?", (libro_id,))
        conn.commit()
