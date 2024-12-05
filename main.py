import tkinter as tk
from tkinter import ttk
from interfaz.autores_interfaz import iniciar_interfaz_autores
from interfaz.libros_interfaz import iniciar_interfaz_libros
from interfaz.prestamos_interfaz import iniciar_interfaz_prestamos

def iniciar_aplicacion():
    root = tk.Tk()
    root.title("Gestión de Biblioteca")
    root.geometry("800x700")
    root.resizable(False, False)

    #crear un frame principal 
    frame_principal = ttk.Frame(root, padding="12 12 12 12")
    frame_principal.grid(row=0, column=0, sticky="nsew")

    # Configurar el estilo
    estilo = ttk.Style()
    estilo.theme_use('clam')
    estilo.configure("TButton", padding=6, relief="flat", background="#ccc")

    # Crear un notebook (pestañas)
    notebook = ttk.Notebook(frame_principal)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Crear los frames para cada sección
    frame_autores = ttk.Frame(notebook)
    frame_libros = ttk.Frame(notebook)
    frame_prestamos = ttk.Frame(notebook)
    frame_acerca_de = ttk.Frame(notebook)

    # Añadir las pestañas al notebook
    notebook.add(frame_autores, text="Autores")
    notebook.add(frame_libros, text="Libros")
    notebook.add(frame_prestamos, text="Préstamos")
    notebook.add(frame_acerca_de, text="Acerca de")

    #configurar la expansión de las columnas y filas
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=1)

    # Inicializar las interfaces de cada sección
    iniciar_interfaz_autores(frame_autores)
    iniciar_interfaz_libros(frame_libros)
    iniciar_interfaz_prestamos(frame_prestamos)

    # Contenido de la pestaña "Acerca de"
    label_acerca_de = ttk.Label(frame_acerca_de, text=(
        "Aplicación tipo escritorio de Gestión de Biblioteca.\n"
        "Proyecto final de programación Python intermedio de Tecno 3F.\n"
        "Este proyecto tiene como objetivo gestionar una biblioteca digital\n"
        "permitiendo operaciones CRUD (crear, leer, actualizar, eliminar)\n"
        "sobre libros, autores y préstamos.\n\n\n"
        "Realizado por Nahir Mabel Caridi, 2024"
    ), justify="center", padding=20)
    label_acerca_de.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
