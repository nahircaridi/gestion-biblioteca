import sqlite3

def create_tables():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Autores (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        nacionalidad TEXT NOT NULL,
        fecha_nacimiento TEXT NOT NULL,
        genero TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Libros (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor_id INTEGER NOT NULL,
        ano_publicacion INTEGER NOT NULL,
        genero TEXT NOT NULL,
        editorial TEXT NOT NULL,
        estado TEXT NOT NULL,
        FOREIGN KEY (autor_id) REFERENCES Autores(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prestamos (
        id INTEGER PRIMARY KEY,
        libro_id INTEGER NOT NULL,
        fecha_prestamo TEXT NOT NULL,
        fecha_devolucion TEXT NOT NULL,
        usuario TEXT NOT NULL,
        FOREIGN KEY (libro_id) REFERENCES Libros(id)
    )''')

    conn.commit()
    conn.close()
    print("Tablas creadas exitosamente")

if __name__ == "__main__":
    create_tables()
