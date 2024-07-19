import tkinter as tk
from tkinter import messagebox, ttk
from DAO import DAO

class Juego(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Infinity Creations - Prototipo juego de rol")
        self.geometry("800x600")
        self.dao = DAO()
        self.widgets()

    def widgets(self):
        
        self.user_button = tk.Button(self, text="Usuario", command=self.opciones_usuario)
        self.user_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.character_button = tk.Button(self, text="Personaje", command=self.opciones_personaje)
        self.character_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.gm_button = tk.Button(self, text="GM", command=self.opciones_gm)
        self.gm_button.pack(side=tk.LEFT, padx=5, pady=5)

    def opciones_usuario(self):
        user_window = tk.Toplevel(self)
        user_window.title("Opciones Usuario")
        user_window.geometry("300x200")
        
        tk.Button(user_window, text="Logear", command=self.logear_usuario).pack(pady=10)
        tk.Button(user_window, text="Registrar", command=self.registrar_usuario).pack(pady=10)

    def opciones_personaje(self):
        character_window = tk.Toplevel(self)
        character_window.title("Opciones Personaje")
        character_window.geometry("300x200")
        
        tk.Button(character_window, text="Mostrar", command=self.mostrar_personajes).pack(pady=10)
        tk.Button(character_window, text="Crear", command=self.crear_personaje).pack(pady=10)

    def opciones_gm(self):
        gm_window = tk.Toplevel(self)
        gm_window.title("Opciones GM")
        gm_window.geometry("300x400")
        
        tk.Button(gm_window, text="Informe GM", command=self.informe_gm).pack(pady=10)
        tk.Button(gm_window, text="Agregar Habilidad", command=self.agregar_habilidad).pack(pady=10)
        tk.Button(gm_window, text="Editar Habilidad", command=self.editar_habilidad).pack(pady=10)
        tk.Button(gm_window, text="Agregar Equipamiento", command=self.agregar_equipamiento).pack(pady=10)
        tk.Button(gm_window, text="Agregar Poder", command=self.agregar_poder).pack(pady=10)
        tk.Button(gm_window, text="Editar Poder", command=self.editar_poder).pack(pady=10)
        tk.Button(gm_window, text="Subir Nivel", command=self.subir_nivel).pack(pady=10)
        tk.Button(gm_window, text="Cambiar Estado", command=self.cambiar_estado).pack(pady=10)

    
    def logear_usuario(self):
        login_window = tk.Toplevel(self)
        login_window.title("Logear Usuario")
        login_window.geometry("300x200")
        
        tk.Label(login_window, text="Usuario").pack(pady=5)
        usuario_entry = tk.Entry(login_window)
        usuario_entry.pack(pady=5)
        
        tk.Label(login_window, text="Contraseña").pack(pady=5)
        contrasenia_entry = tk.Entry(login_window, show='*')
        contrasenia_entry.pack(pady=5)
        
        def logear():
            usuario = usuario_entry.get()
            contrasenia = contrasenia_entry.get()
            if self.dao.logear_usuario(usuario, contrasenia):
                messagebox.showinfo("Éxito", "Usuario logeado correctamente")
                login_window.destroy()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        
        tk.Button(login_window, text="Logear", command=logear).pack(pady=20)

    def registrar_usuario(self):
        register_window = tk.Toplevel(self)
        register_window.title("Registrar Usuario")
        register_window.geometry("300x300")
        
        tk.Label(register_window, text="Nombre Usuario").pack(pady=5)
        nombre_usuario_entry = tk.Entry(register_window)
        nombre_usuario_entry.pack(pady=5)
        
        tk.Label(register_window, text="Contraseña").pack(pady=5)
        contrasenia_entry = tk.Entry(register_window, show='*')
        contrasenia_entry.pack(pady=5)
        
        tk.Label(register_window, text="Tipo Usuario").pack(pady=5)
        tipo_usuario_entry = tk.Entry(register_window)
        tipo_usuario_entry.pack(pady=5)
        
        def registrar():
            nombre_usuario = nombre_usuario_entry.get()
            contrasenia = contrasenia_entry.get()
            tipo_usuario = tipo_usuario_entry.get()
            try:
                self.dao.registrar_usuario(nombre_usuario, contrasenia, tipo_usuario)
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                register_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(register_window, text="Registrar", command=registrar).pack(pady=20)

    def crear_personaje(self):
        create_window = tk.Toplevel(self)
        create_window.title("Crear Personaje")
        create_window.geometry("400x400")
        
        tk.Label(create_window, text="Nombre Personaje").pack(pady=5)
        nombre_personaje_entry = tk.Entry(create_window)
        nombre_personaje_entry.pack(pady=5)
        
        tk.Label(create_window, text="Nombre Jugador").pack(pady=5)
        nombre_jugador_entry = tk.Entry(create_window)
        nombre_jugador_entry.pack(pady=5)
        
        tk.Label(create_window, text="ID Raza").pack(pady=5)
        id_raza_entry = tk.Entry(create_window)
        id_raza_entry.pack(pady=5)
        
        tk.Label(create_window, text="Nivel").pack(pady=5)
        nivel_entry = tk.Entry(create_window)
        nivel_entry.pack(pady=5)
        
        tk.Label(create_window, text="ID Estado").pack(pady=5)
        id_estado_entry = tk.Entry(create_window)
        id_estado_entry.pack(pady=5)
        
        tk.Label(create_window, text="ID Usuario").pack(pady=5)
        id_usuario_entry = tk.Entry(create_window)
        id_usuario_entry.pack(pady=5)
        
        def registrar_personaje():
            nombre_personaje = nombre_personaje_entry.get()
            nombre_jugador = nombre_jugador_entry.get()
            id_raza = id_raza_entry.get()
            nivel = nivel_entry.get()
            id_estado = id_estado_entry.get()
            id_usuario = id_usuario_entry.get()
            try:
                self.dao.registrar_personaje(nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario)
                messagebox.showinfo("Éxito", "Personaje registrado correctamente")
                create_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(create_window, text="Registrar Personaje", command=registrar_personaje).pack(pady=20)

    def mostrar_personajes(self):
        personajes = self.dao.mostrar_personajes()
        mostrar_window = tk.Toplevel(self)
        mostrar_window.title("Personajes")
        mostrar_window.geometry("800x400")

        columns = ("ID", "Nombre", "Jugador", "Raza", "Nivel", "Estado", "Usuario")
        tree = ttk.Treeview(mostrar_window, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        for personaje in personajes:
            
            tree.insert("", "end", values=personaje)
        
        tree.pack(fill=tk.BOTH, expand=True)
        tree.bind("<Double-1>", self.ventanita)


    def ventanita(self, event):
        item = event.widget.selection()[0]
        personaje = event.widget.item(item, "values")
        
        edit_window = tk.Toplevel(self)
        edit_window.title("Editar Personaje")
        edit_window.geometry("400x400")
        
        tk.Label(edit_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(edit_window)
        id_personaje_entry.insert(0, personaje[0])
        id_personaje_entry.pack(pady=5)
        id_personaje_entry.config(state='disabled')
        
        tk.Label(edit_window, text="Nombre Personaje").pack(pady=5)
        nombre_personaje_entry = tk.Entry(edit_window)
        nombre_personaje_entry.insert(0, personaje[1])
        nombre_personaje_entry.pack(pady=5)
        
        tk.Label(edit_window, text="Nombre Jugador").pack(pady=5)
        nombre_jugador_entry = tk.Entry(edit_window)
        nombre_jugador_entry.insert(0, personaje[2])
        nombre_jugador_entry.pack(pady=5)
        
        tk.Label(edit_window, text="ID Raza").pack(pady=5)
        id_raza_entry = tk.Entry(edit_window)
        id_raza_entry.insert(0, personaje[3])
        id_raza_entry.pack(pady=5)
        
        tk.Label(edit_window, text="Nivel").pack(pady=5)
        nivel_entry = tk.Entry(edit_window)
        nivel_entry.insert(0, personaje[4])
        nivel_entry.pack(pady=5)
        
        tk.Label(edit_window, text="ID Estado").pack(pady=5)
        id_estado_entry = tk.Entry(edit_window)
        id_estado_entry.insert(0, personaje[5])
        id_estado_entry.pack(pady=5)
        
        tk.Label(edit_window, text="ID Usuario").pack(pady=5)
        id_usuario_entry = tk.Entry(edit_window)
        id_usuario_entry.insert(0, personaje[6])
        id_usuario_entry.pack(pady=5)
        
        def guardar_cambios():
            id_personaje = id_personaje_entry.get()
            nombre_personaje = nombre_personaje_entry.get()
            nombre_jugador = nombre_jugador_entry.get()
            id_raza = id_raza_entry.get()
            nivel = nivel_entry.get()
            id_estado = id_estado_entry.get()
            id_usuario = id_usuario_entry.get()
            try:
                self.dao.editar_personaje(id_personaje, nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario)
                messagebox.showinfo("Éxito", "Personaje actualizado correctamente")
                edit_window.destroy()
                self.mostrar_personajes()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(edit_window, text="Guardar Cambios", command=guardar_cambios).pack(pady=20)
    
    def informe_gm(self):
        informe = self.dao.informe_gm()
        informe_window = tk.Toplevel(self)
        informe_window.title("Informe GM")
        informe_window.geometry("700x400")  

        columns = ("ID Personaje", "Nombre Personaje", "Raza", "Nivel", "Estado")
        tree = ttk.Treeview(informe_window, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140)
        
        for info in informe:
            
            tree.insert("", "end", values=info)
        
        tree.pack(fill=tk.BOTH, expand=True)


    def agregar_habilidad(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            id_habilidad = id_habilidad_entry.get()
            try:
                self.dao.agregar_habilidad_gm(id_personaje, id_habilidad)
                messagebox.showinfo("Éxito", "Habilidad agregada correctamente")
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        add_window = tk.Toplevel(self)
        add_window.title("Agregar Habilidad")
        add_window.geometry("300x200")

        tk.Label(add_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(add_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(add_window, text="ID Habilidad").pack(pady=5)
        id_habilidad_entry = tk.Entry(add_window)
        id_habilidad_entry.pack(pady=5)

        tk.Button(add_window, text="Agregar", command=submit).pack(pady=20)

    def editar_habilidad(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            id_habilidad = id_habilidad_entry.get()
            nueva_habilidad = nueva_habilidad_entry.get()
            try:
                self.dao.editar_habilidad_gm(id_personaje, id_habilidad, nueva_habilidad)
                messagebox.showinfo("Éxito", "Habilidad editada correctamente")
                edit_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        edit_window = tk.Toplevel(self)
        edit_window.title("Editar Habilidad")
        edit_window.geometry("300x200")

        tk.Label(edit_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(edit_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(edit_window, text="ID Habilidad").pack(pady=5)
        id_habilidad_entry = tk.Entry(edit_window)
        id_habilidad_entry.pack(pady=5)

        tk.Label(edit_window, text="Nueva Habilidad").pack(pady=5)
        nueva_habilidad_entry = tk.Entry(edit_window)
        nueva_habilidad_entry.pack(pady=5)

        tk.Button(edit_window, text="Editar", command=submit).pack(pady=20)

    def agregar_equipamiento(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            id_equipamiento = id_equipamiento_entry.get()
            try:
                self.dao.agregar_equipamiento_gm(id_personaje, id_equipamiento)
                messagebox.showinfo("Éxito", "Equipamiento agregado correctamente")
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        add_window = tk.Toplevel(self)
        add_window.title("Agregar Equipamiento")
        add_window.geometry("300x200")

        tk.Label(add_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(add_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(add_window, text="ID Equipamiento").pack(pady=5)
        id_equipamiento_entry = tk.Entry(add_window)
        id_equipamiento_entry.pack(pady=5)

        tk.Button(add_window, text="Agregar", command=submit).pack(pady=20)

    def agregar_poder(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            id_poder = id_poder_entry.get()
            try:
                self.dao.agregar_poder_gm(id_personaje, id_poder)
                messagebox.showinfo("Éxito", "Poder agregado correctamente")
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        add_window = tk.Toplevel(self)
        add_window.title("Agregar Poder")
        add_window.geometry("300x200")

        tk.Label(add_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(add_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(add_window, text="ID Poder").pack(pady=5)
        id_poder_entry = tk.Entry(add_window)
        id_poder_entry.pack(pady=5)

        tk.Button(add_window, text="Agregar", command=submit).pack(pady=20)

    def editar_poder(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            id_poder = id_poder_entry.get()
            nuevo_poder = nuevo_poder_entry.get()
            try:
                self.dao.editar_poder_gm(id_personaje, id_poder, nuevo_poder)
                messagebox.showinfo("Éxito", "Poder editado correctamente")
                edit_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        edit_window = tk.Toplevel(self)
        edit_window.title("Editar Poder")
        edit_window.geometry("300x200")

        tk.Label(edit_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(edit_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(edit_window, text="ID Poder").pack(pady=5)
        id_poder_entry = tk.Entry(edit_window)
        id_poder_entry.pack(pady=5)

        tk.Label(edit_window, text="Nuevo Poder").pack(pady=5)
        nuevo_poder_entry = tk.Entry(edit_window)
        nuevo_poder_entry.pack(pady=5)

        tk.Button(edit_window, text="Editar", command=submit).pack(pady=20)

    def subir_nivel(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            nuevo_nivel = nuevo_nivel_entry.get()
            try:
                self.dao.subir_nivel_gm(id_personaje, nuevo_nivel)
                messagebox.showinfo("Éxito", "Nivel subido correctamente")
                level_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        level_window = tk.Toplevel(self)
        level_window.title("Subir Nivel")
        level_window.geometry("300x200")

        tk.Label(level_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(level_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(level_window, text="Nuevo Nivel").pack(pady=5)
        nuevo_nivel_entry = tk.Entry(level_window)
        nuevo_nivel_entry.pack(pady=5)

        tk.Button(level_window, text="Subir Nivel", command=submit).pack(pady=20)

    def cambiar_estado(self):
        def submit():
            id_personaje = id_personaje_entry.get()
            nuevo_estado = nuevo_estado_entry.get()
            try:
                self.dao.cambiar_estado_gm(id_personaje, nuevo_estado)
                messagebox.showinfo("Éxito", "Estado cambiado correctamente")
                state_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        state_window = tk.Toplevel(self)
        state_window.title("Cambiar Estado")
        state_window.geometry("300x200")

        tk.Label(state_window, text="ID Personaje").pack(pady=5)
        id_personaje_entry = tk.Entry(state_window)
        id_personaje_entry.pack(pady=5)

        tk.Label(state_window, text="Nuevo Estado").pack(pady=5)
        nuevo_estado_entry = tk.Entry(state_window)
        nuevo_estado_entry.pack(pady=5)

        tk.Button(state_window, text="Cambiar Estado", command=submit).pack(pady=20)

if __name__ == "__main__":
    app = Juego()
    app.mainloop()
