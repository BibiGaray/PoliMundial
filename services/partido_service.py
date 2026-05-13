from models.equipo import Equipo
def registrar_equipo(pais):
    nombre = input("Ingrese el nombre del país: ")
    abrev = input("Ingrese abreviatura del país: ")
    iden = input("Ingrese identificación del país: ")
    telef = input("Ingrese prefijo telefónico del país: ")
    confederacion = input("Ingrese confederación del país: ")
    grupo = input("Ingrese grupo del país: ")
    team = Equipo(nombre, abrev, iden, telef, confederacion, grupo)

    return team