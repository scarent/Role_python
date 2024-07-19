class psje():
    def __init__(self, id_personaje, nombre_personaje, nombre_jugador, id_raza, nivel, id_estado, id_usuario):
        self.__id_personaje = id_personaje
        self.__nombre_personaje = nombre_personaje
        self.__nombre_jugador = nombre_jugador
        self.__id_raza = id_raza
        self.__nivel = 1
        self.__id_estado = id_estado
        self.__id_usuario = id_usuario
        self.__habilidades=[]
        self.__equipamiento = None
        self.__poder=None
    #get
    def get_id_personaje(self):
        return self.__id_personaje

    def get_nombre_personaje(self):
        return self.__nombre_personaje

    def get_nombre_jugador(self):
        return self.__nombre_jugador

    def get_id_raza(self):
        return self.__id_raza

    def get_nivel(self):
        return self.__nivel

    def get_id_estado(self):
        return self.__id_estado

    def get_id_usuario(self):
        return self.__id_usuario

    #set
    def set_id_personaje(self, id_personaje):
        self.__id_personaje = id_personaje

    def set_nombre_personaje(self, nombre_personaje):
        self.__nombre_personaje = nombre_personaje

    def set_nombre_jugador(self, nombre_jugador):
        self.__nombre_jugador = nombre_jugador

    def set_id_raza(self, id_raza):
        self.__id_raza = id_raza

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_id_estado(self, id_estado):
        self.__id_estado = id_estado

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def agregar_habilidad(self,habilidad):
        if len(self.__habilidades) < 2:
            self.__habilidades.append(habilidad)
        else:
            raise Exception("un personaje puede tener 2 habilidades")
    def asignar_equipamiento(self,equipamiento):
        if self.__equipamiento is None:
            self.__equipamiento=equipamiento
        else:
            raise Exception("un Personaje solo puede tener un equipamiento")
    def asignar_poder(self,poder):
        if self.__poder is None:
            self.__poder = poder
        else:
            raise Exception("un personaje solo puede tener un poder")
    def set_estado_inicial(self):
        self.__id_estado=1

class Cusuario():
     def __init__(self, id_usuario, nombre_usuario, contrasenia, tipo_usuario):
        self.__id_usuario = id_usuario
        self.__nombre_usuario = nombre_usuario
        self.__contrasenia = contrasenia
        self.__tipo_usuario = tipo_usuario

    # get
     def get_id_usuario(self):
        return self.__id_usuario

     def get_nombre_usuario(self):
        return self.__nombre_usuario

     def get_contrasenia(self):
        return self.__contrasenia

     def get_tipo_usuario(self):
        return self.__tipo_usuario

    # Set
     def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

     def set_nombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario

     def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

     def set_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario

class Raza():
    def __init__(self, id_raza, nombre_raza):
        self.__id_raza = id_raza
        self.__nombre_raza = nombre_raza

    # Get
    def get_id_raza(self):
        return self.__id_raza

    def get_nombre_raza(self):
        return self.__nombre_raza

    # Set
    def set_id_raza(self, id_raza):
        self.__id_raza = id_raza

    def set_nombre_raza(self, nombre_raza):
        self.__nombre_raza = nombre_raza

class Estado():
    def __init__(self, id_estado, nombre_estado):
        self.__id_estado = id_estado
        self.__nombre_estado = nombre_estado

    # Get
    def get_id_estado(self):
        return self.__id_estado

    def get_nombre_estado(self):
        return self.__nombre_estado

    # Set
    def set_id_estado(self, id_estado):
        self.__id_estado = id_estado

    def set_nombre_estado(self, nombre_estado):
        self.__nombre_estado = nombre_estado

class Habilidad():
    def __init__(self, id_habilidad, nombre_habilidad, detalle, id_raza): 
        self.__id_habilidad = id_habilidad
        self.__nombre_habilidad = nombre_habilidad
        self.__detalle = detalle
        self.__id_raza = id_raza

    # Get
    def get_id_habilidad(self):
        return self.__id_habilidad

    def get_nombre_habilidad(self):
        return self.__nombre_habilidad

    def get_detalle(self):
        return self.__detalle

    def get_id_raza(self):
        return self.__id_raza

    # Set
    def set_id_habilidad(self, id_habilidad):
        self.__id_habilidad = id_habilidad

    def set_nombre_habilidad(self, nombre_habilidad):
        self.__nombre_habilidad = nombre_habilidad

    def set_detalle(self, detalle):
        self.__detalle = detalle

    def set_id_raza(self, id_raza):
        self.__id_raza = id_raza
class Poder():
    def __init__(self, id_poder, nombre_poder, detalle, id_raza):
        self.__id_poder = id_poder
        self.__nombre_poder = nombre_poder
        self.__detalle = detalle
        self.__id_raza = id_raza

    # Get
    def get_id_poder(self):
        return self.__id_poder

    def get_nombre_poder(self):
        return self.__nombre_poder

    def get_detalle(self):
        return self.__detalle

    def get_id_raza(self):
        return self.__id_raza

    # Set
    def set_id_poder(self, id_poder):
        self.__id_poder = id_poder

    def set_nombre_poder(self, nombre_poder):
        self.__nombre_poder = nombre_poder

    def set_detalle(self, detalle):
        self.__detalle = detalle

    def set_id_raza(self, id_raza):
        self.__id_raza = id_raza

class Equipamiento():
    def __init__(self, id_equipamiento, nombre_equipamiento):
        self.__id_equipamiento = id_equipamiento
        self.__nombre_equipamiento = nombre_equipamiento

    # Getters
    def get_id_equipamiento(self):
        return self.__id_equipamiento

    def get_nombre_equipamiento(self):
        return self.__nombre_equipamiento

    # Set
    def set_id_equipamiento(self, id_equipamiento):
        self.__id_equipamiento = id_equipamiento

    def set_nombre_equipamiento(self, nombre_equipamiento):
        self.__nombre_equipamiento = nombre_equipamiento

class Personaje_Habilidad():
    def __init__(self, id_personaje, id_habilidad):
        self.__id_personaje = id_personaje
        self.__id_habilidad = id_habilidad

    # Get
    def get_id_personaje(self):
        return self.__id_personaje

    def get_id_habilidad(self):
        return self.__id_habilidad

    # Set
    def set_id_personaje(self, id_personaje):
        self.__id_personaje = id_personaje

    def set_id_habilidad(self, id_habilidad):
        self.__id_habilidad = id_habilidad

class Personaje_Poder():
    def __init__(self, id_personaje, id_poder):
        self.__id_personaje = id_personaje
        self.__id_poder = id_poder

    # Get
    def get_id_personaje(self):
        return self.__id_personaje

    def get_id_poder(self):
        return self.__id_poder

    # Set
    def set_id_personaje(self, id_personaje):
        self.__id_personaje = id_personaje

    def set_id_poder(self, id_poder):
        self.__id_poder = id_poder

class Personaje_Equipamiento():
    def __init__(self, id_personaje, id_equipamiento):
        self.__id_personaje = id_personaje
        self.__id_equipamiento = id_equipamiento

    # Get
    def get_id_personaje(self):
        return self.__id_personaje

    def get_id_equipamiento(self):
        return self.__id_equipamiento

    # Set
    def set_id_personaje(self, id_personaje):
        self.__id_personaje = id_personaje

    def set_id_equipamiento(self, id_equipamiento):
        self.__id_equipamiento = id_equipamiento