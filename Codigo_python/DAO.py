import mysql.connector

class DAO:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def conectar(self):
        self.__conexion = mysql.connector.connect(
            host='sql10.freesqldatabase.com',
            user='sql10720721',
            password='N23YcgEqlW',
            database='sql10720721'
        )
        self.__cursor = self.__conexion.cursor()

    def cerrar(self):
        self.__cursor.close()
        self.__conexion.close()

    def registrar_usuario(self, nombre_usuario, contrasenia, tipo_usuario):
        self.conectar()
        sql = "INSERT INTO Usuario (nombre_usuario, contrasenia, tipo_usuario) VALUES (%s, %s, %s)"
        values = (nombre_usuario, contrasenia, tipo_usuario)
        self.__cursor.execute(sql, values)
        self.__conexion.commit()
        self.cerrar()

    def logear_usuario(self, nombre_usuario, contrasenia):
        self.conectar()
        sql = "SELECT * FROM Usuario WHERE nombre_usuario = %s AND contrasenia = %s"
        values = (nombre_usuario, contrasenia)
        self.__cursor.execute(sql, values)
        result = self.__cursor.fetchone()
        self.cerrar()
        return result is not None

    def mostrar_personajes(self):
        self.conectar()
        sql = """SELECT 
                    Personaje.id_personaje, 
                    Personaje.nombre_personaje, 
                    Personaje.nombre_jugador, 
                    Raza.nombre_raza, 
                    Personaje.nivel, 
                    Estado.nombre_estado,
                    GROUP_CONCAT(DISTINCT Habilidad.nombre_habilidad) AS habilidades,
                    GROUP_CONCAT(DISTINCT Poder.nombre_poder) AS poderes
                FROM 
                    Personaje
                JOIN 
                    Raza ON Personaje.id_raza = Raza.id_raza
                JOIN 
                    Estado ON Personaje.id_estado = Estado.id_estado
                LEFT JOIN 
                    Personaje_Habilidad ON Personaje.id_personaje = Personaje_Habilidad.id_personaje
                LEFT JOIN 
                    Habilidad ON Personaje_Habilidad.id_habilidad = Habilidad.id_habilidad
                LEFT JOIN 
                    Personaje_Poder ON Personaje.id_personaje = Personaje_Poder.id_personaje
                LEFT JOIN 
                    Poder ON Personaje_Poder.id_poder = Poder.id_poder
                GROUP BY 
                    Personaje.id_personaje
            """
        self.__cursor.execute(sql)
        informacion = self.__cursor.fetchall()
        self.cerrar()
        return informacion



    def informe_gm(self):
        self.conectar()
        sql = """SELECT Personaje.id_personaje, Personaje.nombre_personaje, Raza.nombre_raza, Personaje.nivel, Estado.nombre_estado
                FROM Personaje
                JOIN Raza ON Personaje.id_raza = Raza.id_raza
                JOIN Estado ON Personaje.id_estado = Estado.id_estado"""
        self.__cursor.execute(sql)
        informacion = self.__cursor.fetchall()
        self.cerrar()
        return informacion


    def agregar_habilidad_gm(self, id_personaje, id_habilidad):
        self.conectar()
        sql = "INSERT INTO Personaje_Habilidad (id_personaje, id_habilidad) VALUES (%s, %s)"
        self.__cursor.execute(sql, (id_personaje, id_habilidad))
        self.__conexion.commit()
        self.cerrar()

    def editar_habilidad_gm(self, id_personaje, id_habilidad, nueva_habilidad):
        self.conectar()
        sql = "UPDATE Personaje_Habilidad SET id_habilidad = %s WHERE id_personaje = %s AND id_habilidad = %s"
        self.__cursor.execute(sql, (nueva_habilidad, id_personaje, id_habilidad))
        self.__conexion.commit()
        self.cerrar()

    def agregar_equipamiento_gm(self, id_personaje, id_equipamiento):
        self.conectar()
        sql = "INSERT INTO Personaje_Equipamiento (id_personaje, id_equipamiento) VALUES (%s, %s)"
        self.__cursor.execute(sql, (id_personaje, id_equipamiento))
        self.__conexion.commit()
        self.cerrar()

    def agregar_poder_gm(self, id_personaje, id_poder):
        self.conectar()
        sql = "INSERT INTO Personaje_Poder (id_personaje, id_poder) VALUES (%s, %s)"
        self.__cursor.execute(sql, (id_personaje, id_poder))
        self.__conexion.commit()
        self.cerrar()

    def editar_poder_gm(self, id_personaje, id_poder, nuevo_poder):
        self.conectar()
        sql = "UPDATE Personaje_Poder SET id_poder = %s WHERE id_personaje = %s AND id_poder = %s"
        self.__cursor.execute(sql, (nuevo_poder, id_personaje, id_poder))
        self.__conexion.commit()
        self.cerrar()

    def subir_nivel_gm(self, id_personaje, nuevo_nivel):
        self.conectar()
        sql = "UPDATE Personaje SET nivel = %s WHERE id_personaje = %s AND nivel < %s"
        self.__cursor.execute(sql, (nuevo_nivel, id_personaje, nuevo_nivel))
        self.__conexion.commit()
        self.cerrar()

    def cambiar_estado_gm(self, id_personaje, nuevo_estado):
        self.conectar()
        sql = "UPDATE Personaje SET id_estado = %s WHERE id_personaje = %s"
        self.__cursor.execute(sql, (nuevo_estado, id_personaje))
        self.__conexion.commit()
        self.cerrar()
    def registrar_personaje(self, nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario):
        self.conectar()
        sql = "INSERT INTO Personaje (nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario)
        self.__cursor.execute(sql, values)
        self.__conexion.commit()
        self.cerrar()

    def actualizar_personaje(self, id_personaje, nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario):
        self.conectar()
        sql = "UPDATE Personaje SET nombre_personaje = %s, nombre_jugador = %s, id_raza = %s, nivel = %s, id_estado = %s, id_usuario = %s WHERE id_personaje = %s"
        values = (nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario, id_personaje)
        self.__cursor.execute(sql, values)
        self.__conexion.commit()
        self.cerrar()
    
    


