import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from crud.autores import add_autor, get_autores, update_autor, delete_autor
import datetime
import re 

def iniciar_interfaz_autores(frame):
    def generar_listas_fecha():
        dias = list(range(1, 32))
        meses = list(range(1, 13))
        anio_actual = datetime.datetime.now().year
        anios = list(range(anio_actual - 1000, anio_actual + 1))
        anios.sort(reverse=True)  # Ordenar años de manera descendente
        return dias, meses, anios

    dias, meses, anios = generar_listas_fecha()

    def limitar_longitud_y_texto(entry, limit):
        def validar(texto):
            if len(texto) > limit:
                return False
            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ ]*$", texto):
                return False
            return True
        
        vcmd = (frame.register(validar), '%P')
        entry.config(validate="key", validatecommand=vcmd)

    # Campos de entrada para autores
    ttk.Label(frame, text="Nombre").grid(column=0, row=0, sticky=tk.W)
    entry_nombre = ttk.Entry(frame,width=30)
    entry_nombre.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud_y_texto(entry_nombre, 50)

    ttk.Label(frame, text="Apellido").grid(column=0, row=1, sticky=tk.W)
    entry_apellido = ttk.Entry(frame,width=30)
    entry_apellido.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud_y_texto(entry_apellido, 50)

    ttk.Label(frame, text="Nacionalidad").grid(column=0, row=2, sticky=tk.W)
    entry_nacionalidad = ttk.Entry(frame,width=30)
    entry_nacionalidad.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud_y_texto(entry_nacionalidad, 50)

    ttk.Label(frame, text="Fecha de Nacimiento").grid(column=0, row=3, sticky=tk.W)
    frame_fecha_nacimiento = ttk.Frame(frame)
    frame_fecha_nacimiento.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=10, pady=5)
    combobox_dia = ttk.Combobox(frame_fecha_nacimiento, values=dias, width=5, state='readonly')
    combobox_dia.grid(column=0, row=0, padx=(0, 1))
    combobox_mes = ttk.Combobox(frame_fecha_nacimiento, values=meses, width=5, state='readonly')
    combobox_mes.grid(column=1, row=0, padx=(1, 1))
    combobox_anio = ttk.Combobox(frame_fecha_nacimiento, values=anios, width=7, state='readonly')
    combobox_anio.grid(column=2, row=0, padx=(1, 0))

    ttk.Label(frame, text="Género").grid(column=0, row=4, sticky=tk.W)
    frame_genero = ttk.Frame(frame)
    frame_genero.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=10, pady=5)
    genero = tk.StringVar()
    ttk.Radiobutton(frame_genero, text="Masculino", variable=genero, value="Masculino").grid(column=0, row=0, padx=(0, 5))
    ttk.Radiobutton(frame_genero, text="Femenino", variable=genero, value="Femenino").grid(column=1, row=0, padx=(5, 5))
    ttk.Radiobutton(frame_genero, text="Otro", variable=genero, value="Otro").grid(column=2, row=0, padx=(5, 0))

    ttk.Label(frame, text="ID").grid(column=0, row=5, sticky=tk.W)
    entry_id = ttk.Entry(frame, state='readonly')
    entry_id.grid(column=1, row=5, sticky=(tk.W, tk.E), padx=10, pady=5)

    def limpiar_campos():
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_nacionalidad.delete(0, tk.END)
        combobox_dia.set('')
        combobox_mes.set('')
        combobox_anio.set('')
        genero.set(None)
        entry_id.config(state=tk.NORMAL)
        entry_id.delete(0, tk.END)
        entry_id.config(state='readonly')

    def agregar_autor():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        nacionalidad = entry_nacionalidad.get()
        fecha_nacimiento = f"{combobox_anio.get()}-{combobox_mes.get()}-{combobox_dia.get()}"
        gen = genero.get()

        # Validaciones
        if not nombre or not apellido:
            messagebox.showerror("Error", "Los campos Nombre y Apellido son obligatorios.")
            return
        
        add_autor(nombre, apellido, nacionalidad, fecha_nacimiento, gen)
        actualizar_lista_autores()
        limpiar_campos()

        # Mensaje de éxito
        messagebox.showinfo("Éxito", "¡Autor agregado con éxito!")

    def cargar_autor(event):
        try:
            limpiar_campos()
            item = lista_autores.selection()[0]
            autor = lista_autores.item(item, 'values')
            entry_id.config(state=tk.NORMAL)
            entry_id.insert(0, autor[0])
            entry_id.config(state='readonly')
            entry_nombre.insert(0, autor[1])
            entry_apellido.insert(0, autor[2])
            entry_nacionalidad.insert(0, autor[3])
            fecha_nacimiento = autor[4].split('-')
            combobox_anio.set(fecha_nacimiento[0])
            combobox_mes.set(fecha_nacimiento[1])
            combobox_dia.set(fecha_nacimiento[2])
            genero.set(autor[5])
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un autor para editar.")

    def actualizar_autor():
        try:
            autor_id = entry_id.get()
            if autor_id:  # Verificar que el ID no esté vacío
                autor_id = int(autor_id)
                nombre = entry_nombre.get()
                apellido = entry_apellido.get()
                nacionalidad = entry_nacionalidad.get()
                fecha_nacimiento = f"{combobox_anio.get()}-{combobox_mes.get()}-{combobox_dia.get()}"
                gen = genero.get()

                update_autor(autor_id, nombre, apellido, nacionalidad, fecha_nacimiento, gen)
                actualizar_lista_autores()
                limpiar_campos()

                # Mensaje de éxito
                messagebox.showinfo("Éxito", "¡Autor actualizado con éxito!")
            else:
                raise IndexError
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un autor para actualizar.")

    def eliminar_autor():
        try:
            item = lista_autores.selection()[0]
            autor = lista_autores.item(item, 'values')
            autor_id = autor[0]

            confirmacion = messagebox.askyesno("Confirmación", "¿Seguro que quieres eliminar el autor seleccionado?")
            if confirmacion:  # Solo elimina si el usuario elige "Sí"
                delete_autor(int(autor_id))
                actualizar_lista_autores()
                limpiar_campos()

                # Mensaje de éxito
                messagebox.showinfo("Éxito", "¡Autor eliminado con éxito!")
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un autor para eliminar.")
        
    # Botones para CRUD de autores
    tk.Button(frame, text="Agregar Autor", command=agregar_autor, background='#4CAF50', foreground='white').grid(column=1, row=6, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Actualizar Autor", command=actualizar_autor, background='#FFC107', foreground='black').grid(column=1, row=7, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Eliminar Autor", command=eliminar_autor, background='#F44336', foreground='white').grid(column=1, row=8, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Editar Autor", command=lambda: cargar_autor(None)).grid(column=1, row=9, pady=10, padx=10, sticky="ew")

    #configurar la expansión de la columna 0 del frame
    frame.grid_columnconfigure(0, weight=1)

    # Lista de autores
    columnas_autores = ("ID", "Nombre", "Apellido", "Nacionalidad", "Fecha de Nacimiento", "Género")
    lista_autores = ttk.Treeview(frame, columns=columnas_autores, show="headings")
    
    # Configurar las columnas de la lista
    lista_autores.column("ID", width=50, anchor=tk.CENTER)  
    lista_autores.column("Nombre", width=100, anchor=tk.W)  
    lista_autores.column("Apellido", width=120, anchor=tk.W)  
    lista_autores.column("Nacionalidad", width=130, anchor=tk.W) 
    lista_autores.column("Fecha de Nacimiento", width=120, anchor=tk.W)  
    lista_autores.column("Género", width=80, anchor=tk.W)  
    
    for col in columnas_autores:
        lista_autores.heading(col, text=col)
    lista_autores.grid(column=0, row=10, columnspan=2, sticky="nsew")

    # Configurar la expansión de la fila y las columnas del frame
    frame.grid_rowconfigure(10, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    lista_autores.bind("<Double-1>", cargar_autor)

    def actualizar_lista_autores():
        for i in lista_autores.get_children():
            lista_autores.delete(i)
        autores = get_autores()
        for autor in autores:
            lista_autores.insert("", "end", values=autor)

    actualizar_lista_autores()

    