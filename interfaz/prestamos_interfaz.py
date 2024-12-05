import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  
from crud.prestamos import add_prestamo, get_prestamos, update_prestamo, delete_prestamo
import datetime

def iniciar_interfaz_prestamos(frame):
    def generar_listas_fecha():
        dias = list(range(1, 32))
        meses = list(range(1, 13))
        anio_actual = datetime.datetime.now().year
        anios = list(range(anio_actual - 1000, anio_actual + 1))
        anios.sort(reverse=True)  
        return dias, meses, anios

    dias, meses, anios = generar_listas_fecha()

    def limitar_longitud(entry, limit):
        def validar(texto):
            if len(texto) > limit:
                return False
            return True
        
        vcmd = (frame.register(validar), '%P')
        entry.config(validate="key", validatecommand=vcmd)

    # Campos de entrada para préstamos
    ttk.Label(frame, text="Libro ID").grid(column=0, row=0, sticky=tk.W)
    entry_libro_id = ttk.Entry(frame,width=30)
    entry_libro_id.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=10, pady=5)  
    limitar_longitud(entry_libro_id, 50)

    ttk.Label(frame, text="Fecha de Préstamo").grid(column=0, row=1, sticky=tk.W)
    frame_fecha_prestamo = ttk.Frame(frame)
    frame_fecha_prestamo.grid(column=1, row=1, padx=10, pady=5, sticky="w")
    combobox_dia_prestamo = ttk.Combobox(frame_fecha_prestamo, values=dias, width=5, state='readonly')
    combobox_dia_prestamo.grid(column=0, row=0, padx=(0,1))
    combobox_mes_prestamo = ttk.Combobox(frame_fecha_prestamo, values=meses, width=5, state='readonly')
    combobox_mes_prestamo.grid(column=1, row=0, padx=(1,1))
    combobox_anio_prestamo = ttk.Combobox(frame_fecha_prestamo, values=anios, width=7, state='readonly')
    combobox_anio_prestamo.grid(column=2, row=0, padx=(1,0))

    ttk.Label(frame, text="Fecha de Devolución").grid(column=0, row=2, sticky=tk.W)
    frame_fecha_devolucion = ttk.Frame(frame)
    frame_fecha_devolucion.grid(column=1, row=2, padx=10, pady=5, sticky="w")
    combobox_dia_devolucion = ttk.Combobox(frame_fecha_devolucion, values=dias, width=5, state='readonly')
    combobox_dia_devolucion.grid(column=0, row=0, padx=(0,1))
    combobox_mes_devolucion = ttk.Combobox(frame_fecha_devolucion, values=meses, width=5, state='readonly')
    combobox_mes_devolucion.grid(column=1, row=0, padx=(1,1))
    combobox_anio_devolucion = ttk.Combobox(frame_fecha_devolucion, values=anios, width=7, state='readonly')
    combobox_anio_devolucion.grid(column=2, row=0, padx=(1,0))

    ttk.Label(frame, text="Usuario").grid(column=0, row=3, sticky=tk.W)
    entry_usuario = ttk.Entry(frame, width=30)
    entry_usuario.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=10, pady=5)
    limitar_longitud(entry_usuario, 50)
    
    # Función para limpiar campos del formulario
    def limpiar_campos():
        entry_libro_id.delete(0, tk.END)
        combobox_dia_prestamo.set('')
        combobox_mes_prestamo.set('')
        combobox_anio_prestamo.set('')
        combobox_dia_devolucion.set('')
        combobox_mes_devolucion.set('')
        combobox_anio_devolucion.set('')
        entry_usuario.delete(0, tk.END)

    # Función para agregar préstamo con verificación y mensaje de éxito
    def agregar_prestamo():
        libro_id = entry_libro_id.get()
        fecha_prestamo = f"{combobox_anio_prestamo.get()}-{combobox_mes_prestamo.get()}-{combobox_dia_prestamo.get()}"
        fecha_devolucion = f"{combobox_anio_devolucion.get()}-{combobox_mes_devolucion.get()}-{combobox_dia_devolucion.get()}"
        usuario = entry_usuario.get()
        
        # Validaciones
        if not libro_id or not fecha_prestamo or not usuario:
            messagebox.showerror("Error", "Los campos Libro ID, Fecha de Préstamo y Usuario son obligatorios.")
            return
        
        add_prestamo(libro_id, fecha_prestamo, fecha_devolucion, usuario)
        actualizar_lista_prestamos()
        limpiar_campos()

        # Mensaje de éxito
        messagebox.showinfo("Éxito", "¡Préstamo guardado con éxito!")

    # Función para cargar datos del préstamo seleccionado en los campos de entrada
    def cargar_prestamo(event):
        try:
            limpiar_campos()
            item = lista_prestamos.selection()[0]
            prestamo = lista_prestamos.item(item, 'values')
            entry_libro_id.insert(0, prestamo[1])
            fecha_prestamo = prestamo[2].split('-')
            combobox_anio_prestamo.set(fecha_prestamo[0])
            combobox_mes_prestamo.set(fecha_prestamo[1])
            combobox_dia_prestamo.set(fecha_prestamo[2])
            fecha_devolucion = prestamo[3].split('-')
            combobox_anio_devolucion.set(fecha_devolucion[0])
            combobox_mes_devolucion.set(fecha_devolucion[1])
            combobox_dia_devolucion.set(fecha_devolucion[2])
            entry_usuario.insert(0, prestamo[4])
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un préstamo para editar.")

    # Función para actualizar préstamo con mensaje de éxito
    def actualizar_prestamo():
        try:
            item = lista_prestamos.selection()[0]
            prestamo = lista_prestamos.item(item, 'values')
            prestamo_id = prestamo[0]
            libro_id = entry_libro_id.get()
            fecha_prestamo = f"{combobox_anio_prestamo.get()}-{combobox_mes_prestamo.get()}-{combobox_dia_prestamo.get()}"
            fecha_devolucion = f"{combobox_anio_devolucion.get()}-{combobox_mes_devolucion.get()}-{combobox_dia_devolucion.get()}"
            usuario = entry_usuario.get()

            if not libro_id or not fecha_prestamo or not usuario:
                messagebox.showerror("Error", "Los campos Libro ID, Fecha de Préstamo y Usuario son obligatorios.")
                return
            
            update_prestamo(prestamo_id, libro_id, fecha_prestamo, fecha_devolucion, usuario)
            actualizar_lista_prestamos()
            limpiar_campos()

        # Mensaje de éxito
            messagebox.showinfo("Éxito", "¡Préstamo actualizado con éxito!")
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un préstamo para actualizar.")
    
    # Función para eliminar préstamo con confirmación y mensaje de éxito
    def eliminar_prestamo():
        try:
            # Verificar si hay un préstamo seleccionado en la lista
            item = lista_prestamos.selection()[0]
            prestamo = lista_prestamos.item(item, 'values')
            prestamo_id = prestamo[0]

            confirmacion = messagebox.askyesno("Confirmación", "¿Seguro que quieres eliminar el préstamo seleccionado?")
            if confirmacion:  # Solo elimina si el usuario elige "Sí"
                prestamo_id = int(prestamo_id)
                delete_prestamo(prestamo_id)
                actualizar_lista_prestamos()
                limpiar_campos()
                # Mensaje de éxito
                messagebox.showinfo("Éxito", "¡Préstamo eliminado con éxito!")
        except IndexError:
            # Mostrar error si no hay un préstamo seleccionado
            messagebox.showerror("Error", "Por favor, selecciona un préstamo para eliminar.")

    # Botones para CRUD de préstamos
    tk.Button(frame, text="Agregar Préstamo", command=agregar_prestamo, background='#4CAF50', foreground='white').grid(column=1, row=5, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Actualizar Préstamo", command=actualizar_prestamo, background='#FFC107', foreground='black').grid(column=1, row=6, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Eliminar Préstamo", command=eliminar_prestamo, background='#F44336', foreground='white').grid(column=1, row=7, pady=5, padx=10, sticky="ew")
    tk.Button(frame, text="Editar Préstamo", command=lambda: cargar_prestamo(None)).grid(column=1, row=8, pady=10, padx=10, sticky="ew")

    frame.grid_columnconfigure(0, weight=1)    

    # Lista de préstamos
    columnas_prestamos = ("ID", "Libro ID", "Fecha de Préstamo", "Fecha de Devolución", "Usuario")
    lista_prestamos = ttk.Treeview(frame, columns=columnas_prestamos, show="headings")
    
    #configurar las columnas de la lista
    lista_prestamos.column("ID", width=50, anchor=tk.CENTER)
    lista_prestamos.column("Libro ID", width=50, anchor=tk.CENTER)
    lista_prestamos.column("Fecha de Préstamo", width=50, anchor=tk.W)
    lista_prestamos.column("Fecha de Devolución", width=50, anchor=tk.W)
    lista_prestamos.column("Usuario", width=100, anchor=tk.W)
    
    for col in columnas_prestamos:
        lista_prestamos.heading(col, text=col)

    lista_prestamos.grid(column=0, row=9, columnspan=2, sticky="nsew")

    # Configurar expansión de columnas y filas
    frame.grid_rowconfigure(9, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # Vincular la selección de la lista a la función cargar_prestamo
    lista_prestamos.bind("<Double-1>", cargar_prestamo)

    # Función para actualizar la lista de préstamos
    def actualizar_lista_prestamos():
        for i in lista_prestamos.get_children():
            lista_prestamos.delete(i)
        prestamos = get_prestamos()
        for prestamo in prestamos:
            lista_prestamos.insert("", "end", values=prestamo)

    # Actualizar la lista de préstamos al iniciar
    actualizar_lista_prestamos()
