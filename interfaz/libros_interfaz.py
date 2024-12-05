import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from crud.libros import add_libro, get_libros, update_libro, delete_libro

def iniciar_interfaz_libros(frame):
    generos = ["Arte", "Autoayuda", "Aventura", "Biografía", "Ciencia ficción", "Cocina", "Contemporáneo", "Fantasía", "Histórico", "Infantil", "Juvenil", "Misterio", "Poesía", "Romántico", "Salud/Deporte", "Técnico/Especializado", "Terror", "Thriller"]

    def limitar_longitud_y_numerico(entry, limit):
        def validar(texto):
            if len(texto) > limit:
                return False
            if texto == "":
                return True
            if not texto.isdigit():
                return False
            return True
        
        vcmd = (frame.register(validar), '%P')
        entry.config(validate="key", validatecommand=vcmd)

    def limitar_longitud(entry, limit):
        def validar(texto):
            if len(texto) > limit:
                return False
            return True
            
        vcmd = (frame.register(validar), '%P')
        entry.config(validate="key", validatecommand=vcmd)

    # Campos de entrada para libros
    ttk.Label(frame, text="Título").grid(column=0, row=0, sticky=tk.W)
    entry_titulo = ttk.Entry(frame, width=30)
    entry_titulo.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud(entry_titulo, 100)

    ttk.Label(frame, text="Autor ID").grid(column=0, row=1, sticky=tk.W)
    entry_autor_id = ttk.Entry(frame, width=30)
    entry_autor_id.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=10, pady=5)

    ttk.Label(frame, text="Año Publicación").grid(column=0, row=2, sticky=tk.W)
    entry_ano_publicacion = ttk.Entry(frame, width=30)
    entry_ano_publicacion.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud_y_numerico(entry_ano_publicacion, 4)

    ttk.Label(frame, text="Género").grid(column=0, row=3, sticky=tk.W)
    combobox_genero = ttk.Combobox(frame, values=generos, state='readonly', width=30)
    combobox_genero.grid(column=1, row=3, padx=10, pady=5)

    ttk.Label(frame, text="Editorial").grid(column=0, row=4, sticky=tk.W)
    entry_editorial = ttk.Entry(frame, width=30)
    entry_editorial.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud(entry_editorial, 50)

    ttk.Label(frame, text="Estado").grid(column=0, row=5, sticky=tk.W)
    estado = tk.StringVar()
    # Crear un marco para los Radiobutton
    frame_estado = ttk.Frame(frame)
    frame_estado.grid(column=1, row=5, sticky=tk.W, padx=220, pady=5)

    # Agregar los Radiobutton al marco
    ttk.Radiobutton(frame_estado, text="Disponible", variable=estado, value="Disponible").grid(column=0, row=0, padx=20, sticky=tk.W)
    ttk.Radiobutton(frame_estado, text="Prestado", variable=estado, value="Prestado").grid(column=1, row=0, padx=20, sticky=tk.W)

    ttk.Label(frame, text="ID").grid(column=0, row=6, sticky=tk.W)
    entry_id = ttk.Entry(frame, state='readonly', width=30)
    entry_id.grid(column=1, row=6, sticky=(tk.W, tk.E), padx=10, pady=5)

    # Función para limpiar campos del formulario
    def limpiar_campos():
        entry_titulo.delete(0, tk.END)
        entry_autor_id.delete(0, tk.END)
        entry_ano_publicacion.delete(0, tk.END)
        combobox_genero.set('')
        entry_editorial.delete(0, tk.END)
        estado.set(None)
        entry_id.config(state=tk.NORMAL)
        entry_id.delete(0, tk.END)
        entry_id.config(state='readonly')

    # Función para agregar libro con verificación
    def agregar_libro():
        titulo = entry_titulo.get()
        autor_id = entry_autor_id.get()
        ano_publicacion = entry_ano_publicacion.get()
        genero = combobox_genero.get()
        editorial = entry_editorial.get()
        estado_libro = estado.get()

        # Verificación de campos obligatorios
        if not titulo or not autor_id or not estado_libro:
            messagebox.showerror("Error", "Los campos Título, Autor ID y Estado son obligatorios.")
            return

        add_libro(titulo, autor_id, ano_publicacion, genero, editorial, estado_libro)
        actualizar_lista_libros()
        limpiar_campos()

        # Mensaje de éxito
        messagebox.showinfo("Éxito", "¡Libro guardado con éxito!")

    # Función para cargar datos del libro seleccionado en los campos de entrada
    def cargar_libro(event):
        try:
            limpiar_campos()
            item = lista_libros.selection()[0]
            libro = lista_libros.item(item, 'values')
            entry_id.config(state=tk.NORMAL)
            entry_id.insert(0, libro[0])
            entry_id.config(state='readonly')
            entry_titulo.insert(0, libro[1])
            entry_autor_id.insert(0, libro[2])
            entry_ano_publicacion.insert(0, libro[3])
            combobox_genero.set(libro[4])
            entry_editorial.insert(0, libro[5])
            estado.set(libro[6])
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un libro para editar.")

    # Función para actualizar libro con verificación
    def actualizar_libro():
        try:
            libro_id = entry_id.get()
            if libro_id:  # Verificar que el ID no esté vacío
                libro_id = int(libro_id)
                titulo = entry_titulo.get()
                autor_id = entry_autor_id.get()
                ano_publicacion = entry_ano_publicacion.get()
                genero = combobox_genero.get()
                editorial = entry_editorial.get()
                estado_libro = estado.get()

            # Verificación de campos obligatorios
                if not titulo or not autor_id or not estado_libro:
                    messagebox.showerror("Error", "Los campos Título, Autor ID y Estado son obligatorios.")
                    return

                update_libro(libro_id, titulo, autor_id, ano_publicacion, genero, editorial, estado_libro)
                actualizar_lista_libros()
                limpiar_campos()

            # Mensaje de éxito
                messagebox.showinfo("Éxito", "¡Libro actualizado con éxito!")
            else:
                raise IndexError
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un libro para actualizar.")

    # Función para eliminar libro con confirmación directa desde la lista
    def eliminar_libro():
        try:
            # Verificar si hay un libro seleccionado en la lista
            item = lista_libros.selection()[0]
            libro = lista_libros.item(item, 'values')
            libro_id = libro[0]

            confirmacion = messagebox.askyesno("Confirmación", "¿Seguro que quieres eliminar el libro seleccionado?")
            if confirmacion:  # Solo elimina si el usuario elige "Sí"
                libro_id = int(libro_id)
                delete_libro(libro_id)
                actualizar_lista_libros()
                limpiar_campos()
                # Mensaje de éxito
                messagebox.showinfo("Éxito", "¡Libro eliminado con éxito!")
        except IndexError:
            # Mostrar error si no hay un libro seleccionado
            messagebox.showerror("Error", "Por favor, selecciona un libro para eliminar.")

    # Botones para CRUD de libros con colores específicos
    tk.Button(frame, text="Agregar Libro", command=agregar_libro, background='#4CAF50', foreground='white').grid(column=1, row=7, pady= 5, padx=10, sticky="ew")
    tk.Button(frame, text="Actualizar Libro", command=actualizar_libro, background='#FFC107', foreground='black').grid(column=1, row=8, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Eliminar Libro", command=eliminar_libro, background='#F44336', foreground='white').grid(column=1, row=9, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Editar Libro", command=lambda: cargar_libro(None)).grid(column=1, row=10, pady=10, padx=10, sticky="ew")

    frame.grid_columnconfigure(0, weight=1)

    # Lista de libros
    columnas_libros = ("ID", "Título", "Autor ID", "Año Publicación", "Género", "Editorial", "Estado")
    lista_libros = ttk.Treeview(frame, columns=columnas_libros, show="headings")

    #configurar las columnas de la lista
    lista_libros.column("ID", width=50, anchor=tk.CENTER)  
    lista_libros.column("Título", width=200, anchor=tk.W)  
    lista_libros.column("Autor ID", width=80, anchor=tk.CENTER)  
    lista_libros.column("Año Publicación", width=100, anchor=tk.CENTER)
    lista_libros.column("Género", width=100, anchor=tk.W)
    lista_libros.column("Editorial", width=150, anchor=tk.W)
    lista_libros.column("Estado", width=80, anchor=tk.W)

    for col in columnas_libros:
        lista_libros.heading(col, text=col)

    lista_libros.grid(column=0, row=11, columnspan=2, sticky="nsew")

    # Configurar expansión de la fila y las columnas del frame
    frame.grid_rowconfigure(11, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # Vincular la selección de la lista a la función cargar_libro
    lista_libros.bind("<Double-1>", cargar_libro)

    # Función para actualizar la lista de libros
    def actualizar_lista_libros():
        for i in lista_libros.get_children():
            lista_libros.delete(i)
        libros = get_libros()
        for libro in libros:
            lista_libros.insert("", "end", values=libro)

    # Actualizar la lista de libros al iniciar
    actualizar_lista_libros()
