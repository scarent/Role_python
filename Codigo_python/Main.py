import tkinter as tk
from DAO import DAO
from Atributos import *



def Usuario():
    id_usuario = 1+2
    print(id_usuario)
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    print(nombre_usuario)
    contrasenia= input("Ingrese una contraseña: ")
    print(contrasenia)
    tipo_usuario=input("GM o Jugador")
    print(tipo_usuario)
    US_lista = Cusuario(id_usuario,nombre_usuario,contrasenia,tipo_usuario)
    d = DAO()
    print("DAO Iniciado")
    d.Registrar_usuario(US_lista)
    print("Usuario Registrado con exito")

'--habilidades-- & --equipamiento--'
def obtener_habilidad():
    id_habilidad = input("Ingrese el ID de la habilidad: ")
    nombre_habilidad = input("Ingrese el nombre de la habilidad: ")
    detalle = input("Ingrese el detalle de la habilidad: ")
    id_raza = input("Ingrese el ID de la raza: ")
    return Habilidad(id_habilidad,nombre_habilidad,detalle,id_raza)

def obtener_equipamiento():
    equipamiento=[]
    for i in range(8):
        id_equipamiento= i+1
        nombre_equipamiento=f"Equipamiento {i+1}"
        equipamiento.append(Equipamiento(id_equipamiento,nombre_equipamiento))
    return equipamiento

def poderes():
    poderes=[]
    for i in range(4):
        id_poder=i+1
        nombre_poder=f"poder{i+1}"
        detalle=f"Detalle del poder {i+1}"
        id_raza=1
        poderes.append(Poder(id_poder,nombre_poder,detalle,id_raza))
    return poderes


def habilidades_iniciales():
    habilidad1=habilidad(1,"habilidad 1","Detalle 1",1)
    habilidad2=habilidad(2,"habilidad 2","Detalle 2",1)
    return [habilidad1,habilidad2]
def equipamiento_inicial():
    return Equipamiento(1,"Espada Inicial")

def poder_inicial():
    return Poder(1,"poder inicial","detalle del poder",1)
"--Habilidades por raza--"
def ls_habilidades_raza():
    c=DAO()
    habilidades=c.ls_habilidades_raza()
    for habilidad in habilidades:
        nombre_raza,nombre_habilidad,detalle = habilidad
        print(f"Raza: {nombre_raza},Habilidad: {nombre_habilidad},Detalle:{detalle}")

'--Poderes Por raza--'
def ls_poderes_raza():
    C=DAO()
    poderes=C.lis_poderes_raza()
    for poder in poderes:
        nombre_raza,nombre_poder,detalle=poder
    print(f"Raza:{nombre_raza},Poder:{nombre_poder},Detalle{detalle}")


'--FuncionesGM--'
def agregar_habilidad_gm(id_personaje):
    habilidad=obtener_habilidad()
    c=DAO()
    print("DAO iniciado")
    c.agregar_habilidad_gm(id_personaje,habilidad)
    print("habilidad agregada con exito")

def editar_habilidad_gm(id_personaje,id_habilidad):
    nueva_habilidad=obtener_habilidad()#puede ser habilidad
    c=DAO()
    print("DAO Iniciado")
    c.editar_habilidad(id_personaje,id_habilidad,nueva_habilidad[0])
    print("habilidad editada con exito")

def agregar_equipamiento_gm(id_personaje):
    equipamiento=obtener_equipamiento()
    c=DAO()
    print("DAO iniciado")
    c.agregar_equipamiento(id_personaje,equipamiento[0])
    print("Equipamiento agregado con exito")

def editar_poder_gm(id_personaje,id_poder):
    nuevo_poder=poderes()
    c=DAO()
    print("DAO iniciado")
    c.editar_poder(id_personaje,id_poder,nuevo_poder)
    print("poder editado con exito")

def subir_nivel_gm(id_personaje,nuevo_nivel):
    c = DAO()
    print("DAO iniciado")
    c.subir_nivel(id_personaje,nuevo_nivel)
    print("Nivel subido con exito")

def cambiar_estado_gm(id_personaje,nuevo_estado):
    c=DAO()
    print("DAO Iniciado")
    c.cambiar_estado(id_personaje,nuevo_estado)
    print("estado cambiado con exito")

'--Crud--'

def registrar():
    id_personaje = None
    N_personaje = input("Ingrese el nombre de su personaje: ")
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    id_raza = input("Id raza: ") 
    nivel = 1
    id_estado = 1
    id_usuario= input("id usuario ")
    PJ_lista = psje(id_personaje,N_personaje,nombre_jugador,id_raza,nivel,id_estado,id_usuario)
    c = DAO()
    print("DAO iniciado")
    c.registrar(PJ_lista)
    print("Se registro con exito")
def mostrar():
    d=DAO()
    lista=d.Mostrar()
    for valor in lista:
        print(valor)
def InGm():
    f= DAO()
    lista = f.InGm()
    for valor in lista:
        nombre_personaje,id_raza,nivel,id_estado=valor
        print(f"Nombre:{nombre_personaje}, Raza:{id_raza},Nivel:{nivel},Estado:{id_estado}")
    

def menu_gm():
    print("--MENU GM--")
    print("1-. ADD HABILIDAD")
    print("2-. EDITAR HABILIDAD")
    print("3-. AGREGAR EQUIPAMIENTO")
    print("4-. ADD poder")
    print("5-. Editar poder")
    print("6-. Subir NLV")
    print("7-. CAmbiar estado")
    print("8-. Listar Habilidades por Raza")
    print("9-. Listar poderes por raza")
    op = input("ingrese una opcion: ")
    if op =='1':
        id_personaje= input("Ingrese el Id del personaje: ")
        agregar_habilidad_gm(id_personaje)
    elif op=='2':
        id_personaje= input("Ingrese el Id del personaje: ")
        id_habilidad=input("Ingrese el id de la habilidad a editar: ")
        editar_habilidad_gm(id_personaje,id_habilidad)
    elif op=='3':
        id_personaje= input("Ingrese el Id del personaje: ")
        agregar_equipamiento_gm(id_personaje)
    elif op=='4':
        id_personaje= input("Ingrese el Id del personaje: ")
        agregar_poder_gm(id_personaje)
    elif op=='5':
        id_personaje= input("Ingrese el Id del personaje: ")
        id_poder= input("Ingrese el id del poder a editar: ")
        editar_poder_gm(id_personaje,id_poder)
    elif op =='6':
        id_personaje= input("Ingrese el Id del personaje: ")
        nuevo_nivel= input("ingrese el nuevo nivel: ")
        nuevo_nivel_gm(id_personaje,nuevo_nivel)
    elif op=='7':
        id_personaje= input("Ingrese el Id del personaje: ")
        nuevo_estado=input('ingrese el nuevo estado: ')
        cambiar_estado_gm(id_personaje,nuevo_estado)
    elif op=="8":
        ls_habilidades_raza()
    elif op =='9':
        ls_poderes_raza()#hay problemas, creo que es la sentencia sql en el DAO

def menu():
    print("-------------seleccione una opcion------------")
    print("1-.  Logear usuario")
    print("2-.  Registrar usuario")
    print("3-.  Mostrar")
    print("4-.  InformeGm ")
    print("5-.  GM")
    print("6-.  ")
    op = input("ingrese una opcion: ")
    if op == "1":
        Usuario()    
    elif op=="2":
        registrar()
    elif op=="3":
        mostrar()
    elif op=="4":
        InGm()
    elif op=="5":
        menu_gm()
    elif op==6:
        return True
    else:
        print("opcion no valida, intentalo otra vez")
        return True
while menu()!=True:
    pass
